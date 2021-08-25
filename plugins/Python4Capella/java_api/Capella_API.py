loadModule('/Capella/Capella')
import sys

def capella_query(query_class, e_obj, cls = None):
    """Call a query from the semantic browser from the qualified class name of the query and the EObect to pass as parameter"""
    res = []
    for e in callQuery(query_class, e_obj.get_java_object()):
        e_object_class = getattr(sys.modules["__main__"], "EObject")
        specific_cls = e_object_class.get_class(e)
        if specific_cls is not None:
            res.append(specific_cls(e))
        elif cls is not None:
            res.append(cls(e))
    return res

def capella_query_by_name(e_obj, query_name, cls = None):
    """Call a query from the semantic browser from the query name and the EObect to pass as parameter"""
    res = []
    for e in getSBQuery(e_obj.get_java_object(), query_name):
        e_object_class = getattr(sys.modules["__main__"], "EObject")
        specific_cls = e_object_class.get_class(e)
        if specific_cls is not None:
            res.append(specific_cls(e))
        elif cls is not None:
            res.append(cls(e))
    return res

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
