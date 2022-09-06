loadModule('/Capella/Sirius')
include('workspace://Python4Capella/java_api/Java_API.py')
if False:
    from java_api.Java_API import *


class Sirius:

    @staticmethod
    def get_representation_descriptors(eObject):
        """Gets the List of RepresentationDescriptor for the given EObject"""
        diagram_class = getattr(sys.modules["__main__"], "Diagram")
        return JavaList(getRepresentationDescriptors(eObject), diagram_class)

    @staticmethod
    def export_image(self, file_path):
        """Exports an image to the given file path from the given RepresentationDescriptor"""
        exportImage(self, file_path)

    @staticmethod
    def load_session(aird_path):
        return loadSiriusSession(aird_path)

    @staticmethod
    def get_system_engineering(session):
        return getEngineering(session)

    @staticmethod
    def get_represented_elements(descriptor):
        e_object_class = getattr(sys.modules["__main__"], "EObject")
        return JavaList(getRepresentedElements(descriptor), e_object_class)

    @staticmethod
    def is_visible_in_documentation(descriptor):
        return isVisibleInDocumentation(descriptor)

    @staticmethod
    def is_visible_for_traceability(descriptor):
        return isVisibleForTraceability(descriptor)

    @staticmethod
    def is_synchronized(descriptor):
        return isSynchronized(descriptor)

    @staticmethod
    def get_status(descriptor):
        return getStatus(descriptor)

    @staticmethod
    def get_review(descriptor):
        return getReview(descriptor)

    @staticmethod
    def get_all_diagrams(session):
        return getAllDiagrams(session)

    @staticmethod
    def get_diagrams(session, cls):
        diagram_class = getattr(sys.modules["__main__"], "Diagram")
        return JavaList(getDiagrams(session, cls), diagram_class)

    @staticmethod
    def get_representing_diagrams(e_object):
        diagram_class = getattr(sys.modules["__main__"], "Diagram")
        return JavaList(getRepresentingDiagrams(e_object), diagram_class)

    @staticmethod
    def get_contextual_element_for_diagrams(e_object):
        diagram_class = getattr(sys.modules["__main__"], "Diagram")
        return JavaList(getContextualElementForDiagrams(e_object), diagram_class)
    
    @staticmethod
    def get_session(e_object):
        return getSession(e_object)
    

    @staticmethod
    def start_transaction(session):
        return startTransaction(session)

    @staticmethod
    def commit_transaction(session):
        return commitTransaction(session)

    @staticmethod
    def rollback_transaction(session):
        return rollbackTransaction(session)
    
    @staticmethod
    def createProgressMonitor():
        return createProgressMonitor()

    @staticmethod
    def get_package(descriptor):
        return getPackage(descriptor)
