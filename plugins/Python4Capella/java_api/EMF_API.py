def eAllContents(e_obj): # provided by org.eclipse.python4capella.modules.EMFModule
    pass
def eAllContentsByType(e_obj, e_class): # provided by org.eclipse.python4capella.modules.EMFModule
    pass
def getEClassifier(ns_uri, eclass_name): # provided by org.eclipse.python4capella.modules.EMFModule
    pass
def create(ns_uri, eclass_name): # provided by org.eclipse.python4capella.modules.EMFModule
    pass
def createFromEClassifier(e_class): # provided by org.eclipse.python4capella.modules.EMFModule
    pass
def getEnumLiteral(ns_uri, enum_name, literal_name): # provided by org.eclipse.python4capella.modules.EMFModule
    pass
def eInverse(e_obj, reference_name): # provided by org.eclipse.python4capella.modules.EMFModule
    pass
def eInverseByType(e_obj, e_classifier): # provided by org.eclipse.python4capella.modules.EMFModule
    pass
def eInverseByName(e_obj, reference_name): # provided by org.eclipse.python4capella.modules.EMFModule
    pass
def copy(e_obj): # provided by org.eclipse.python4capella.modules.EMFModule
    pass
def copyAll(e_objs): # provided by org.eclipse.python4capella.modules.EMFModule
    pass
def delete(e_obj): # provided by org.eclipse.python4capella.modules.EMFModule
    pass
def deleteAll(e_objs): # provided by org.eclipse.python4capella.modules.EMFModule
    pass

loadModule('/Capella/EMF')
include('Java_API.py')
if False:
    from java_api.Java_API import *


def e_all_contents(e_obj):
    """Gets all elements contained directly and indirectly in the given EObject"""
    e_object_class = getattr(sys.modules["__main__"], "EObject")
    return JavaList(eAllContents(e_obj), e_object_class);

def e_all_contents_by_type(e_obj, cls):
    """Gets all elements contained directly and indirectly in the given EObject that are instances of the given cls"""
    return JavaList(eAllContentsByType(e_obj, cls.e_class), cls);


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

def e_inverse(e_obj, cls):
    """Gets the List of object referencing the given EObject"""
    e_object_class = getattr(sys.modules["__main__"], "EObject")
    return JavaList(eInverse(e_obj), e_object_class);

def e_inverse_by_type(e_obj, cls):
    """Gets the List of object referencing the given EObject via an EReference with the given type"""
    return JavaList(eInverseByType(e_obj, cls.e_class), cls);

def e_inverse_by_name(e_obj, reference_name):
    """Gets the List of object referencing the given EObject via an EReference with the given name"""
    e_object_class = getattr(sys.modules["__main__"], "EObject")
    return JavaList(eInverseByName(e_obj, reference_name), e_object_class);

def copy_e_object(e_obj):
    """Copies the given EObject"""
    return copy(e_obj)

def copy_all_e_objects(e_objs):
    """Copies all given EObject"""
    e_object_class = getattr(sys.modules["__main__"], "EObject")
    return JavaList(copyAll(e_objs), e_object_class);

def delete_e_object(e_obj):
    """Deletes the given EObject"""
    return delete(e_obj)

def delete_all_e_objects(e_objs):
    """Deletes all given EObject"""
    return deleteAll(e_objs)
