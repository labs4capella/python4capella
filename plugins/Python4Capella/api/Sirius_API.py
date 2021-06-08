loadModule('/Capella/Sirius')

def get_representation_descriptors_sirius(self):
    return getRepresentationDescriptors(self.get_java_object());
def export_image_sirius(self, file_path):
    exportImage(self.get_java_object(), file_path)
