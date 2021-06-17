loadModule('/Capella/Sirius')

def get_representation_descriptors_sirius(self):
    """Gets the List of RepresentationDescriptor for the given EObject"""
    return getRepresentationDescriptors(self.get_java_object());
def export_image_sirius(self, file_path):
    """Exports an image to the given file path from the given RepresentationDescriptor"""
    exportImage(self.get_java_object(), file_path)
