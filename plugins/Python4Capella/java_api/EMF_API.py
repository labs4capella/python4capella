def eAllContents(e_obj): # provider by org.eclipse.python4capella.modules.EMFModule
    pass
def eAllContentsByType(e_obj, e_class): # provider by org.eclipse.python4capella.modules.EMFModule
    pass
def getEClassifier(ns_uri, eclass_name): # provider by org.eclipse.python4capella.modules.EMFModule
    pass
def create(ns_uri, eclass_name): # provider by org.eclipse.python4capella.modules.EMFModule
    pass
def createFromEClassifier(e_class): # provider by org.eclipse.python4capella.modules.EMFModule
    pass
def getEnumLiteral(ns_uri, enum_name, literal_name): # provider by org.eclipse.python4capella.modules.EMFModule
    pass
def eInverse(e_obj, reference_name): # provider by org.eclipse.python4capella.modules.EMFModule
    pass
def copy(e_obj): # provider by org.eclipse.python4capella.modules.EMFModule
    pass
def copyAll(e_objs): # provider by org.eclipse.python4capella.modules.EMFModule
    pass

loadModule('/Capella/EMF')
include('workspace://Python4Capella/java_api/Java_API.py')
if False:
    from java_api.Java_API import *
import sys


def e_all_contents(e_obj):
    """Gets all elements contained directly and indirectly in the given EObject"""
    e_object_class = getattr(sys.modules["__main__"], "EObject")
    return JavaList(eAllContents(e_obj), e_object_class);

def e_all_contents_by_type(e_obj, cls):
    """Gets all elements contained directly and indirectly in the given EObject that are instances of the given cls"""
    e_object_class = getattr(sys.modules["__main__"], "EObject")
    return JavaList(eAllContentsByType(e_obj, cls.e_class), e_object_class);


def get_e_classifier(ns_uri, eclass_name):
    """Gets the EClassifier for the given namespace URI and eclassifier name"""
    return getEClassifier(ns_uri, eclass_name)


def create_e_object(ns_uri, eclass_name):
    """Creates an EObject of the given type (namespace URI and EClass name)"""
    return create(ns_uri, eclass_name)

def create_e_object_from_e_classifier(e_class):
    """Creates an EObject of the given EClass"""
    return createFromEClassifier(e_class)


def create_e_list(java_list, cls):
    """Creates a JavaList"""
    return JavaList(java_list, cls)


def get_enum_literal(ns_uri, enum_name, literal_name):
    """Gets the enum literal"""
    return getEnumLiteral(ns_uri, enum_name, literal_name)

def e_inverse(e_obj, reference_name):
    """Gets the List of object referencing the given EObject via an EReference with the given name"""
    e_object_class = getattr(sys.modules["__main__"], "EObject")
    return JavaList(eInverse(e_obj, reference_name), e_object_class);

def copy_e_object(e_obj):
    """Copies the given EObject"""
    return copy(e_obj)

def copy_all_e_objects(e_objs):
    """Copies all given EObject"""
    e_object_class = getattr(sys.modules["__main__"], "EObject")
    return JavaList(copyAll(e_objs), e_object_class);
