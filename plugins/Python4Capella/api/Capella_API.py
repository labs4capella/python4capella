loadModule('/Capella/Capella')
import sys

def capella_query(query_class, e_obj):
        res = []
        for e in callQuery(query_class, e_obj.get_java_object()):
            specific_cls = getattr(sys.modules[e_obj.__module__], e.eClass().getName())
            res.append(specific_cls(e))
        return res

def capella_query_by_name(query_class, e_obj):
        res = []
        for e in getSBQuery(query_class, e_obj.get_java_object()):
            specific_cls = getattr(sys.modules[e_obj.__module__], e.eClass().getName())
            res.append(specific_cls(e))
        return res

def available_query_names(e_obj):
    return getAvailableSBQueries(e_obj.get_java_object())

def get_extensions(extensible_element, ns_uri, eclass_name):
    return getExtensions(extensible_element.get_java_object(), ns_uri, eclass_name)
