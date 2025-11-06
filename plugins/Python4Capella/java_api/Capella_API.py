def callQuery(query_class, e_obj): # provided by org.eclipse.python4capella.modules.CapellaModule
    pass
def getSBQuery(e_obj, query_name): # provided by org.eclipse.python4capella.modules.CapellaModule
    pass
def getAvailableSBQueries(e_obj): # provided by org.eclipse.python4capella.modules.CapellaModule
    pass
def getCapellaVersion(): # provided by org.eclipse.python4capella.modules.CapellaModule
    pass
def getLabel(e_obj): # provided by org.eclipse.python4capella.modules.CapellaModule
    pass
def getLibraries(system_engineering): # provided by org.eclipse.python4capella.modules.CapellaModule
    pass
def getExtensions(e_obj, e_class): # provided by org.eclipse.python4capella.modules.CapellaModule
    pass

loadModule('/Capella/Capella')
include('EMF_API.py')
if False:
    from java_api.EMF_API import *

def capella_query(query_class, e_obj, cls = None):
    """Call a query from the semantic browser from the qualified class name of the query and the EObect to pass as parameter"""
    e_object_class = getattr(sys.modules["__main__"], "EObject")
    if cls is None:
        return JavaList(callQuery(query_class, e_obj.get_java_object()), e_object_class)
    else:
        return JavaList(callQuery(query_class, e_obj.get_java_object()), cls)

def capella_query_by_name(e_obj, query_name, cls = None):
    """Call a query from the semantic browser from the query name and the EObject to pass as parameter"""
    e_object_class = getattr(sys.modules["__main__"], "EObject")
    if cls is None:
        return JavaList(getSBQuery(e_obj.get_java_object(), query_name), e_object_class)
    else:
        return JavaList(getSBQuery(e_obj.get_java_object(), query_name), cls)

def available_query_names(e_obj):
    """List all available query names for the given EObject"""
    return getAvailableSBQueries(e_obj.get_java_object())

def capella_version():
    """Gets the current Capella version"""
    return getCapellaVersion()

def get_label(e_obj):
    """Gets the label of the given EObject"""
    return getLabel(e_obj.get_java_object())

def is_system(component):
    res = False

    if get_e_classifier("http://www.polarsys.org/capella/core/cs/" + capella_version(), "Component").isInstance(component):
        if not component.isActor():
            if get_e_classifier("http://www.polarsys.org/capella/core/cs/" + capella_version(), "ComponentPkg").isInstance(component.eContainer()) and get_e_classifier("http://www.polarsys.org/capella/core/cs/" + capella_version(), "BlockArchitecture").isInstance(component.eContainer().eContainer()):
                    eGetValue = component.eContainer().eGet(component.eContainingFeature())
                    if eGetValue.__class__.__name__ == 'JavaList':
                        for comp in eGetValue:
                            if not comp.isActor():
                                res = comp == component
                                break;
        return res;

def get_libraries(system_engineering):
    """Gets the list of libraries for the given system engineering"""
    res = []
    
    if system_engineering is not None:
        lib_cls = getattr(sys.modules["__main__"], "CapellaLibrary")
        e_object_cls = getattr(sys.modules["__main__"], "EObject")
        for value in getLibraries(system_engineering.get_java_object()):
            lib = lib_cls()
            lib.open(e_object_cls(value))
            res.append(lib)
        
    return res

def get_extensions(e_obj, cls):
    """Gets the List of extensions with the given type for the given EObject"""
    return JavaList(getExtensions(e_obj.get_java_object(), cls.e_class), cls);
