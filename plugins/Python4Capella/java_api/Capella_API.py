loadModule('/Capella/Capella')
import sys

def capella_query(query_class, e_obj, cls = None):
    """Call a query from the semantic browser from the qualified class name of the query and the EObect to pass as parameter"""
    res = []
    for e in callQuery(query_class, e_obj.get_java_object()):
        specific_cls = getattr(sys.modules["__main__"], e.eClass().getName())
        if specific_cls is not None:
            res.append(specific_cls(e))
        elif cls is not None:
            res.append(cls(e))
    return res

def capella_query_by_name(query_name, e_obj):
    """Call a query from the semantic browser from the query name and the EObect to pass as parameter"""
    res = []
    for e in getSBQuery(query_name, e_obj.get_java_object()):
        specific_cls = getattr(sys.modules["__main__"], e.eClass().getName())
        if specific_cls is not None:
            res.append(specific_cls(e))
    return res

def available_query_names(e_obj):
    """List all available query names for the given EObject"""
    return getAvailableSBQueries(e_obj.get_java_object())

def capella_version():
    return getCapellaVersion()

def get_label(e_obj):
    return getLabel(e_obj.get_java_object())
