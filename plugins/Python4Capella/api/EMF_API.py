loadModule('/Capella/EMF')
include('workspace://Python4Capella/api/Java_API.py')
if False:
    from api.Java_API import *
import sys

class EObject(JavaObject):
    def delete(self):
        delete(self.get_java_object())
    def e_get(self, feature_name):
        return eGet(self.get_java_object(), feature_name)
    def e_set(self, feature_name, value):
        return eSet(self.get_java_object(), feature_name, value)
    def get_all(self, cls):
        res = []
        for e in e_all_contents(self.get_java_object(), cls.get_e_class()):
            specific_cls = getattr(sys.modules[cls.__module__], e.eClass().getName())
            res.append(specific_cls(e))
        return res
    def e_container(self):
        e = self.get_java_object().eContainer()
        if e is None:
            return e
        else:
            specific_cls = getattr(sys.modules[self.__module__], e.eClass().getName())
            return specific_cls(e)
        
def e_all_contents(e_obj, e_class):
    return eAllContents(e_obj, e_class);
def get_e_classifier(ns_uri, eclass_name):
    return getEClassifier(ns_uri, eclass_name)
def create_e_object(ns_uri, eclass_name):
    return create(ns_uri, eclass_name)
def create_e_list(java_list, cls):
    return JavaList(java_list, cls)