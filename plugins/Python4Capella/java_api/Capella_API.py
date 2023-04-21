def callQuery(query_class, e_obj): # provider by org.eclipse.python4capella.modules.CapellaModule
    pass
def getSBQuery(e_obj, query_name): # provider by org.eclipse.python4capella.modules.CapellaModule
    pass
def getAvailableSBQueries(e_obj): # provider by org.eclipse.python4capella.modules.CapellaModule
    pass
def getCapellaVersion(): # provider by org.eclipse.python4capella.modules.CapellaModule
    pass
def getLabel(e_obj): # provider by org.eclipse.python4capella.modules.CapellaModule
    pass
def isSystem(component): # provider by org.eclipse.python4capella.modules.CapellaModule
    pass
def getLibraries(system_engineering): # provider by org.eclipse.python4capella.modules.CapellaModule
    pass

loadModule('/Capella/Capella')
include('workspace://Python4Capella/java_api/Java_API.py')
if False:
    from java_api.Java_API import *
import sys

def capella_query(query_class, e_obj, cls = None):
    """Call a query from the semantic browser from the qualified class name of the query and the EObect to pass as parameter"""
    e_object_class = getattr(sys.modules["__main__"], "EObject")
    return JavaList(callQuery(query_class, e_obj.get_java_object()), e_object_class)

def capella_query_by_name(e_obj, query_name, cls = None):
    """Call a query from the semantic browser from the query name and the EObect to pass as parameter"""
    e_object_class = getattr(sys.modules["__main__"], "EObject")
    return JavaList(getSBQuery(e_obj.get_java_object(), query_name), e_object_class)

def available_query_names(e_obj):
    """List all available query names for the given EObject"""
    return getAvailableSBQueries(e_obj.get_java_object())

def capella_version():
    return getCapellaVersion()

def get_label(e_obj):
    return getLabel(e_obj.get_java_object())

def is_system(component):
    return isSystem(component)

def get_libraries(system_engineering):
    res = []
    
    if system_engineering is not None:
        lib_cls = getattr(sys.modules["__main__"], "CapellaLibrary")
        for value in getLibraries(system_engineering.get_java_object()):
            lib = lib_cls()
            lib.open(value)
            res.append(lib)
        
    return res
