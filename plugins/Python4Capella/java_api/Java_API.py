loadModule('/Capella/Java')
import sys

class JavaObject:
    """A wrapping class for a Java Object"""
    def __init__(self, java_object):
        self.java_object = java_object
    def get_java_object(self):
        """Gets the Java Object"""
        return self.java_object
    def __eq__(self, other):
        if isinstance(other, JavaObject):
            return self.java_object == other.java_object
        else:
            return False

class JavaIterator(JavaObject):
    """A wrapping class for a Java Iterator"""
    def __init__(self, java_object, cls):
        JavaObject.__init__(self, java_object)
        self.cls = cls;
    def next(self):
        """Gets the next element"""
        if iteratorHasNext(self.get_java_object()):
            next = iteratorNext(self.get_java_object())
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(next)
            return specific_cls(next)
        else:
            raise StopIteration
    def __next__(self):
        return self.next()

class JavaList(JavaObject):
    """A wrapping class for a Java Iterator"""
    def __init__(self, java_object, cls):
        JavaObject.__init__(self, java_object)
        self.cls = cls;
    def __iter__(self):
        return JavaIterator(self.get_java_object().iterator(), self.cls)
    def add(self, obj):
        """Adds the given Object to the list"""
        return self.get_java_object().add(obj.get_java_object())
    def add_all(self, list):
        """Adds all elements of the given List"""
        res = False;
        for e in list:
            res = self.get_java_object().add(e.get_java_object()) or res
        return res
    def remove(self, obj):
        """Removes the given Object"""
        return self.get_java_object().remove(obj.get_java_object())
    def remove_all(self, list):
        """Removes all elements from the given List"""
        res = False;
        for e in list:
            res = self.get_java_object().remove(e.get_java_object()) or res
        return res
    def contains(self, obj):
        """Tells if the given Object is contained in this List"""
        return self.get_java_object().contains(obj.get_java_object())
    def contains_all(self, obj):
        """Tells if all the elements of the given List are contained in this List"""
        for e in list:
            if not self.get_java_object().contains(e.get_java_object()):
                return False
        return True
    def index_of(self, obj):
        """Gets the first index of hte given Object in this List"""
        return self.get_java_object().indexOf(obj.get_java_object())
    def last_index_of(self, obj):
        """Gets the last index of hte given Object in this List"""
        return self.get_java_object().lastIndexOf(obj.get_java_object())
    def get(self, index):
        """Gets the Object at the given index"""
        value = self.get_java_object().get(index)
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            if specific_cls is not None:
                return specific_cls(value)
            else:
                return None
    def clear(self):
        """Removes all elements from this List"""
        return self.get_java_object().clear()
    def size(self):
        """Gets the size of this List"""
        return self.get_java_object().size()
