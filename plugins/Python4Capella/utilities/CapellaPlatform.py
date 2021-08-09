# this script define some utility methods to interact with the Capella platform

# includes needed to interact with the Eclipse platform
loadModule('/System/UI')
loadModule('/System/Resources')

class CapellaPlatform():
    @staticmethod
    def getFirstSelectedElement():
        """
        return the first element select by the user (if several are selected)
        """
        return getSelection().getFirstElement()
    
    @staticmethod
    def getModelPath(elem):
        """
        return the relavite path toward the aird file of a CapellaElement or Diagram
        """
        res = elem.get_java_object().eResource().getURI().toPlatformString(True)
        res = res[1:res.rfind(".")] + ".aird"
        return res
    
    @staticmethod
    def getProject(name):
        """
        retrieve a project defined in the Project Explorer from its name
        """
        return getProject(name)
    
    @staticmethod
    def getFolder(project, folder_name):
        """
        retrieve or create a folder in a project from its name
        """
        folder = project.getFolder(folder_name)
        if not folder.exists():
            folder.create(True, True, None)
        return folder
    
    @staticmethod
    def getAbsolutePath(folder):
        """
        get the absolute path of a folder
        """
        return folder.getLocation().toString()
    
    @staticmethod
    def refresh(folder):
        """
        refresh the content of a folder in the Project Explorer
        """
        refreshResource(folder)