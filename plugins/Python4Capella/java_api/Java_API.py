from typing import TypeVar, Iterator, Any, List
def iteratorHasNext(iterator): # provider by org.eclipse.python4capella.modules.JavaModule
    pass
def iteratorNext(iterator): # provider by org.eclipse.python4capella.modules.JavaModule
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
            return self.java_object == other.java_object
        else:
            return False

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
                return specific_cls(nxt)
            else:
                return self.cls(nxt)
        else:
            raise StopIteration
    def __next__(self) -> T:
        return self.next()

class JavaList(JavaObject, List[T]):
    """A wrapping class for a Java Iterator"""
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
        return self.get_java_object().remove(obj.get_java_object())
    def remove_all(self, l: List[Any]) -> bool:
        """Removes all elements from the given List"""
        res = False;
        for e in l:
            res = self.get_java_object().remove(e.get_java_object()) or res
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
        return self.get(items)
    def get(self, index: int) -> T:
        """Gets the Object at the given index"""
        value = self.get_java_object().get(index)
        if value is None:
            return value
        else:
            specific_cls = self.e_object_class.get_class(value)
            if specific_cls is not None:
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
