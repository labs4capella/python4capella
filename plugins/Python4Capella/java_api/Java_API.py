from typing import TypeVar, Iterator, Any, List, MutableSequence
from operator import index as integer_index
def iteratorHasNext(iterator): # provided by org.eclipse.python4capella.modules.JavaModule
    pass
def iteratorNext(iterator): # provided by org.eclipse.python4capella.modules.JavaModule
    pass
def listRemoveAt(java_list, index): # provided by org.eclipse.python4capella.modules.JavaModule
    pass
def listRemove(java_list, value): # provided by org.eclipse.python4capella.modules.JavaModule
    pass

loadModule('/Capella/Java')
import sys

T = TypeVar("T")

class JavaObject:
    """A wrapping class for a Java Object"""
    def __init__(self, java_object: Any):
        self.java_object = java_object
    def get_java_object(self) -> Any:
        """Gets the Java Object"""
        return self.java_object
    def __eq__(self, other: Any):
        if isinstance(other, JavaObject):
            if self.java_object:
                return self.java_object.equals(other.java_object)
            else:
                return other.java_object is None
        else:
            return False
    def __hash__(self):
        if self.java_object:
            return self.java_object.hashCode()
        else:
            return 0

class JavaIterator(JavaObject,Iterator[T]):
    """A wrapping class for a Java Iterator"""
    def __init__(self, java_object, cls: type):
        JavaObject.__init__(self, java_object)
        self.cls = cls;
        self.e_object_class = getattr(sys.modules["__main__"], "EObject")
    def next(self) -> T:
        """Gets the next element"""
        if iteratorHasNext(self.get_java_object()):
            nxt = iteratorNext(self.get_java_object())
            specific_cls = self.e_object_class.get_class(nxt)
            if specific_cls is not None:
                if hasattr(self.cls, 'e_class') and hasattr(specific_cls, 'e_class') and specific_cls.e_class.isSuperTypeOf(self.cls.e_class):
                    try:
                        return self.cls(nxt)
                    except:
                        return specific_cls(nxt)
                else:
                    return specific_cls(nxt)
            else:
                return self.cls(nxt)
        else:
            raise StopIteration
    def __next__(self) -> T:
        return self.next()

class JavaList(JavaObject, MutableSequence[T]):
    """A mutable sequence backed exclusively by a Java collection.

    Model collections still require a transaction for modifications. The legacy
    remove() method retains its Java boolean result, unlike Python list.remove().
    """
    def __init__(self, java_object: Any, cls: type):
        JavaObject.__init__(self, java_object)
        self.cls = cls;
        self.e_object_class = getattr(sys.modules["__main__"], "EObject")
    def __iter__(self):
        return JavaIterator[T](self.get_java_object().iterator(), self.cls)
    def add(self, obj: T) -> bool:
        """Adds the given Object to the list"""
        return self.get_java_object().add(obj.get_java_object())
    def add_all(self, l: List[T]) -> bool:
        """Adds all elements of the given List"""
        res = False;
        for e in l:
            res = self.get_java_object().add(e.get_java_object()) or res
        return res
    def remove(self, obj: Any) -> bool:
        """Removes the given Object"""
        return listRemove(self.get_java_object(), obj.get_java_object())
    def remove_all(self, l: List[Any]) -> bool:
        """Removes all elements from the given List"""
        res = False;
        for e in l:
            res = listRemove(self.get_java_object(), e.get_java_object()) or res
        return res
    def contains(self, obj: Any) -> bool:
        """Tells if the given Object is contained in this List"""
        return self.get_java_object().contains(obj.get_java_object())
    def contains_all(self, l: List[Any]) -> bool:
        """Tells if all the elements of the given List are contained in this List"""
        for e in l:
            if not self.get_java_object().contains(e.get_java_object()):
                return False
        return True
    def index_of(self, obj: Any) -> int:
        """Gets the first index of hte given Object in this List"""
        return self.get_java_object().indexOf(obj.get_java_object())
    def last_index_of(self, obj: Any) -> int:
        """Gets the last index of hte given Object in this List"""
        return self.get_java_object().lastIndexOf(obj.get_java_object())
    def __getitem__(self, items):
        if isinstance(items, slice):
            return [self.get(i) for i in range(*items.indices(len(self)))]
        return self.get(self._normalize_index(items))
    def _normalize_index(self, index):
        index = integer_index(index)
        size = len(self)
        if index < 0:
            index += size
        if index < 0 or index >= size:
            raise IndexError("JavaList index out of range")
        return index
    def __setitem__(self, index, value):
        if isinstance(index, slice):
            values = list(value)
            # Validate wrappers before modifying the backing collection.
            for item in values:
                item.get_java_object()
            start, stop, step = index.indices(len(self))
            indices = range(start, stop, step)
            if step != 1:
                if len(values) != len(indices):
                    raise ValueError("attempt to assign sequence of size %d to extended slice of size %d"
                                     % (len(values), len(indices)))
                for i, item in zip(indices, values):
                    self[i] = item
            else:
                del self[index]
                for offset, item in enumerate(values):
                    self.insert(start + offset, item)
        else:
            self.get_java_object().set(self._normalize_index(index), value.get_java_object())
    def __delitem__(self, index):
        if isinstance(index, slice):
            for i in sorted(range(*index.indices(len(self))), reverse=True):
                listRemoveAt(self.get_java_object(), i)
        else:
            listRemoveAt(self.get_java_object(), self._normalize_index(index))
    def insert(self, index: int, value: T):
        index = integer_index(index)
        size = len(self)
        if index < 0:
            index = max(0, size + index)
        else:
            index = min(index, size)
        self.get_java_object().add(index, value.get_java_object())
    def extend(self, values):
        # Snapshot first so extending from this same Java collection is safe.
        for value in list(values):
            self.append(value)
    def get(self, index: int) -> T:
        """Gets the Object at the given index"""
        value = self.get_java_object().get(index)
        if value is None:
            return value
        else:
            specific_cls = self.e_object_class.get_class(value)
            if specific_cls is not None:
                if hasattr(self.cls, 'e_class') and hasattr(specific_cls, 'e_class') and specific_cls.e_class.isSuperTypeOf(self.cls.e_class):
                    try:
                        return self.cls(value)
                    except:
                        return specific_cls(value)
                else:
                    return specific_cls(value)
            else:
                return self.cls(value)
    def clear(self) -> bool:
        """Removes all elements from this List"""
        return self.get_java_object().clear()
    def __len__(self) -> int:
        return self.size()
    def len(self) -> int:
        return self.size()
    def size(self) -> int:
        """Gets the size of this List"""
        return self.get_java_object().size()
    def __str__(self) -> str:
        res = "["
        it = self.__iter__()
        while iteratorHasNext(it.get_java_object()):
            res = res + str(it.next())
            if iteratorHasNext(it.get_java_object()):
                res = res + ", "
            
        return res + "]"
    def __repr__(self) -> str:
        return self.__str__()
