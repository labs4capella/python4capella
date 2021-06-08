loadModule('/Capella/Java')
import sys

class JavaObject:
    def __init__(self, java_object):
        self.java_object = java_object
    def get_java_object(self):
        return self.java_object

class JavaIterator(JavaObject):
    def __init__(self, java_object, cls):
        JavaObject.__init__(self, java_object)
        self.cls = cls;
    def next(self):
        if iteratorHasNext(self.get_java_object()):
            next = iteratorNext(self.get_java_object())
            specific_cls = getattr(sys.modules[self.cls.__module__], next.eClass().getName())
            return specific_cls(next)
        else:
            raise StopIteration

class JavaList(JavaObject):
    def __init__(self, java_object, cls):
        JavaObject.__init__(self, java_object)
        self.cls = cls;
    def __iter__(self):
        return JavaIterator(listIterator(self.get_java_object()), self.cls)
    def add(self, obj):
        return listAdd(self.get_java_object(), obj.get_java_object())
    def add_all(self, list):
        res = False;
        for e in list:
            res = listAdd(self.get_java_object(), e.get_java_object()) or res
        return res
    def remove(self, obj):
        return listRemove(self.get_java_object(), obj.get_java_object())
    def remove_all(self, list):
        res = False;
        for e in list:
            res = listRemove(self.get_java_object(), e.get_java_object()) or res
        return res
    def contains(self, obj):
        return listContains(self.get_java_object(), obj.get_java_object())
    def contains_all(self, obj):
        for e in list:
            if not listContains(self.get_java_object(), e.get_java_object()):
                return False
        return True
    def index_of(self, obj):
        return listIndexOf(self.get_java_object(), obj.get_java_object())
    def last_index_of(self, obj):
        return listLastIndexOf(self.get_java_object(), obj.get_java_object())
    def get(self, index):
        return listGet(self.get_java_object(), index)
    def clear(self):
        listClear(self.get_java_object())
    def size(self):
        listSize(self.get_java_object())
