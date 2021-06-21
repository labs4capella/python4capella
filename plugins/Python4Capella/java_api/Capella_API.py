loadModule('/Capella/Capella')
import sys

def capella_query(query_class, e_obj):
    """Call a query from the semantic browser from the qualified class name of the query and the EObect to pass as parameter"""
    res = []
    for e in callQuery(query_class, e_obj.get_java_object()):
        specific_cls = getattr(sys.modules["__main__"], e.eClass().getName())
        res.append(specific_cls(e))
    return res

def capella_query_by_name(query_name, e_obj):
    """Call a query from the semantic browser from the query name and the EObect to pass as parameter"""
    res = []
    for e in getSBQuery(query_name, e_obj.get_java_object()):
        specific_cls = getattr(sys.modules["__main__"], e.eClass().getName())
        res.append(specific_cls(e))
    return res

def available_query_names(e_obj):
    """List all available query names for the given EObject"""
    return getAvailableSBQueries(e_obj.get_java_object())

def get_extensions(extensible_element, ns_uri, eclass_name):
    """Gets the liste of extensions of the given type (namespace URI and EClass name) for the given ExtensibleElement"""
    return getExtensions(extensible_element.get_java_object(), ns_uri, eclass_name)
