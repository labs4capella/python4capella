"""JavaList protocol tests runnable with CPython, without a Capella workspace."""
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


class BackingList:
    """Minimal Java List stand-in; stores raw objects rather than wrappers."""
    def __init__(self, values=()):
        self.values = list(values)

    def size(self):
        return len(self.values)

    def get(self, index):
        return self.values[index]

    def set(self, index, value):
        previous = self.values[index]
        self.values[index] = value
        return previous

    def add(self, *args):
        if len(args) == 1:
            self.values.append(args[0])
            return True
        self.values.insert(*args)

    def remove(self, value):
        if value in self.values:
            self.values.remove(value)
            return True
        return False

    def contains(self, value):
        return value in self.values

    def clear(self):
        self.values.clear()

    def iterator(self):
        return iter(self.values)


class RawObject:
    def equals(self, other):
        return self is other

    def hashCode(self):
        return id(self)


class JavaListTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        source = Path(__file__).resolve().parents[2] / 'plugins/Python4Capella/java_api/Java_API.py'
        cls.namespace = {'loadModule': lambda name: None}
        exec(compile(source.read_text(), str(source), 'exec'), cls.namespace)
        cls.wrapper = cls.namespace['JavaObject']
        cls.list_type = cls.namespace['JavaList']
        # JavaIterator is tested through its public next/iteration protocol.
        class IteratorAdapter:
            def __init__(self, iterator):
                self.iterator = iterator
                self.pending = []
            def has_next(self):
                if not self.pending:
                    try:
                        self.pending.append(next(self.iterator))
                    except StopIteration:
                        return False
                return True
            def next(self):
                if not self.has_next():
                    raise StopIteration
                return self.pending.pop()
        cls.iterator_adapter = IteratorAdapter
        cls.namespace['iteratorHasNext'] = lambda it: it.has_next()
        cls.namespace['iteratorNext'] = lambda it: it.next()
        cls.namespace['listRemoveAt'] = lambda backing, index: backing.values.pop(index)
        cls.namespace['listRemove'] = lambda backing, value: backing.remove(value)

    def setUp(self):
        eobject = type('EObject', (), {'get_class': staticmethod(lambda raw: None)})
        patcher = patch.object(sys.modules['__main__'], 'EObject', eobject, create=True)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.raw = [RawObject() for _ in range(6)]
        self.items = [self.wrapper(raw) for raw in self.raw]
        self.backing = BackingList(self.raw[:3])
        self.backing.iterator = lambda: self.iterator_adapter(iter(self.backing.values))
        self.values = self.list_type(self.backing, self.wrapper)

    def assertContents(self, indices):
        self.assertEqual([self.raw[i] for i in indices], self.backing.values)
        self.assertEqual([self.items[i] for i in indices], list(self.values))
        self.assertEqual(len(indices), len(self.values))

    def test_append_and_membership_use_java_collection(self):
        self.assertIn(self.items[0], self.values)
        self.assertNotIn(self.items[3], self.values)
        self.assertNotIn(object(), self.values)
        self.assertIsNone(self.values.append(self.items[3]))
        self.assertIn(self.items[3], self.values)
        self.assertContents([0, 1, 2, 3])

    def test_insert_clamps_indices(self):
        self.values.insert(-100, self.items[3])
        self.values.insert(100, self.items[4])
        self.values.insert(-1, self.items[5])
        self.assertContents([3, 0, 1, 2, 5, 4])

    def test_indexing_assignment_and_deletion(self):
        self.assertEqual(self.items[2], self.values[-1])
        self.values[-1] = self.items[3]
        del self.values[-2]
        self.assertContents([0, 3])
        self.assertEqual(self.items[3], self.values.pop())
        self.assertContents([0])

    def test_invalid_indices(self):
        for index in (3, -4):
            with self.assertRaises(IndexError):
                self.values[index]
            with self.assertRaises(IndexError):
                self.values[index] = self.items[4]
            with self.assertRaises(IndexError):
                del self.values[index]
        with self.assertRaises(TypeError):
            self.values[1.5]
        self.assertContents([0, 1, 2])

    def test_slices_and_reverse_deletion(self):
        self.assertEqual(self.items[2::-1], self.values[::-1])
        self.assertEqual(self.items[1:3], self.values[1:])
        del self.values[::-2]
        self.assertContents([1])

    def test_slice_assignment(self):
        self.values[1:2] = self.items[3:5]
        self.assertContents([0, 3, 4, 2])
        self.values[3:1] = [self.items[5]]
        self.assertContents([0, 3, 4, 5, 2])
        self.values[:] = self.values
        self.assertContents([0, 3, 4, 5, 2])

    def test_extended_slice_assignment_validates_length(self):
        with self.assertRaises(ValueError):
            self.values[::2] = [self.items[4]]
        self.assertContents([0, 1, 2])
        self.values[::-2] = self.items[3:5]
        self.assertContents([4, 1, 3])

    def test_invalid_slice_value_does_not_delete_elements(self):
        with self.assertRaises(AttributeError):
            self.values[:] = [object()]
        self.assertContents([0, 1, 2])

    def test_extend_and_in_place_addition(self):
        self.values.extend(iter(self.items[3:5]))
        self.values += [self.items[5]]
        self.assertContents([0, 1, 2, 3, 4, 5])

    def test_extend_self(self):
        self.values.extend(self.values)
        self.assertContents([0, 1, 2, 0, 1, 2])

    def test_count_index_and_reverse(self):
        self.values.append(self.items[0])
        self.assertEqual(2, self.values.count(self.items[0]))
        self.assertEqual(1, self.values.index(self.items[1]))
        with self.assertRaises(ValueError):
            self.values.index(self.items[5])
        self.values.reverse()
        self.assertContents([0, 2, 1, 0])

    def test_legacy_methods_keep_boolean_results(self):
        self.assertTrue(self.values.add(self.items[3]))
        self.assertTrue(self.values.contains(self.items[3]))
        self.assertTrue(self.values.remove(self.items[3]))
        self.assertFalse(self.values.remove(self.items[3]))
        self.assertTrue(self.values.add_all(self.items[4:6]))
        self.assertTrue(self.values.remove_all(self.items[4:6]))
        self.assertContents([0, 1, 2])
        self.values.clear()
        self.assertContents([])
        with self.assertRaises(IndexError):
            self.values.pop()


if __name__ == '__main__':
    unittest.main()
