loadModule('/Capella/Sirius')


class Sirius:

    @staticmethod
    def get_representation_descriptors(eObject):
        """Gets the List of RepresentationDescriptor for the given EObject"""
        return getRepresentationDescriptors(eObject);

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
        return getRepresentedElements(descriptor)

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
        return getDiagrams(session, cls)

    @staticmethod
    def get_representing_diagrams(e_object):
        return getRepresentingDiagrams(e_object)

    @staticmethod
    def get_contextual_element_for_diagrams(e_object):
        return getContextualElementForDiagrams(e_object)
    
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
