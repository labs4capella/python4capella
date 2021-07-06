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
    def get_all_diagrams(descriptor):
        return getAllDiagrams(descriptor)

    @staticmethod
    def get_diagrams(descriptor, type):
        return getDiagrams(descriptor, type)
