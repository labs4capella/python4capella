loadModule('/Capella/EMF')
include('workspace://Python4Capella/java_api/Java_API.py')
if False:
    from java_api.Java_API import *
import sys

class EObject(JavaObject):
    """Root class of any model element"""
    def delete(self):
        """Deletes the given EObject"""
        delete(self.get_java_object())
    def get_all(self, cls):
        """Gets all elements of the given Class contained directly and indirectly in the EObject"""
        res = []
        for e in e_all_contents(self.get_java_object()):
            specific_cls = getattr(sys.modules["__main__"], e.eClass().getName())
            value = specific_cls(e)
            if isinstance(value, cls):
                res.append(value)
        return res
    def e_container(self):
        """Gets the container of the EObject"""
        e = self.get_java_object().eContainer()
        if e is None:
            return e
        else:
            specific_cls = getattr(sys.modules["__main__"], e.eClass().getName())
            return specific_cls(e)
        
def e_all_contents(e_obj):
    """Gets all elements contained directly and indirectly in the given EObject"""
    return eAllContents(e_obj);
def get_e_classifier(ns_uri, eclass_name):
    """Gets the EClassifier for the given namespace URI and eclassifier name"""
    return getEClassifier(ns_uri, eclass_name)
def create_e_object(ns_uri, eclass_name):
    """Creates an EObject of the given type (namespace URI and EClass name)"""
    return create(ns_uri, eclass_name)
def create_e_list(java_list, cls):
    """Creates a JavaList"""
    return JavaList(java_list, cls)