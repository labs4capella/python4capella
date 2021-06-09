loadModule('/Capella/Java')
import sys

class JavaObject:
    """A wrapping class for a Java Object"""
    def __init__(self, java_object):
        self.java_object = java_object
    def get_java_object(self):
        """Gets the Java Object"""
        return self.java_object

class JavaIterator(JavaObject):
    """A wrapping class for a Java Iterator"""
    def __init__(self, java_object, cls):
        JavaObject.__init__(self, java_object)
        self.cls = cls;
    def next(self):
        """Gets the next element"""
        if iteratorHasNext(self.get_java_object()):
            next = iteratorNext(self.get_java_object())
            specific_cls = getattr(sys.modules[self.cls.__module__], next.eClass().getName())
            return specific_cls(next)
        else:
            raise StopIteration

class JavaList(JavaObject):
    """A wrapping class for a Java Iterator"""
    def __init__(self, java_object, cls):
        JavaObject.__init__(self, java_object)
        self.cls = cls;
    def __iter__(self):
        return JavaIterator(listIterator(self.get_java_object()), self.cls)
    def add(self, obj):
        """Adds the given Object to the list"""
        return listAdd(self.get_java_object(), obj.get_java_object())
    def add_all(self, list):
        """Adds all elements of the given List"""
        res = False;
        for e in list:
            res = listAdd(self.get_java_object(), e.get_java_object()) or res
        return res
    def remove(self, obj):
        """Removes the given Object"""
        return listRemove(self.get_java_object(), obj.get_java_object())
    def remove_all(self, list):
        """Removes all elements from the given List"""
        res = False;
        for e in list:
            res = listRemove(self.get_java_object(), e.get_java_object()) or res
        return res
    def contains(self, obj):
        """Tells if the given Object is contained in this List"""
        return listContains(self.get_java_object(), obj.get_java_object())
    def contains_all(self, obj):
        """Tells if all the elements of the given List are contained in this List"""
        for e in list:
            if not listContains(self.get_java_object(), e.get_java_object()):
                return False
        return True
    def index_of(self, obj):
        """Gets the first index of hte given Object in this List"""
        return listIndexOf(self.get_java_object(), obj.get_java_object())
    def last_index_of(self, obj):
        """Gets the last index of hte given Object in this List"""
        return listLastIndexOf(self.get_java_object(), obj.get_java_object())
    def get(self, index):
        """Gets the Object at the given index"""
        return listGet(self.get_java_object(), index)
    def clear(self):
        """Removes all elements from this List"""
        listClear(self.get_java_object())
    def size(self):
        """Gets the size of this List"""
        listSize(self.get_java_object())
