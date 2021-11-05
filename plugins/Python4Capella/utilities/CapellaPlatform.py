# this script define some utility methods to interact with the Capella platform

# includes needed to interact with the Eclipse platform
loadModule('/System/UI')
loadModule('/System/Resources')

include('workspace://Python4Capella/java_api/Sirius_API.py')
if False:
    from java_api.Sirius_API import *

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
        return the relative path toward the aird file of a CapellaElement or Diagram
        """
        res = Sirius.get_session(elem.java_object).getSessionResource().getURI().toPlatformString(True)
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
    
    @staticmethod
    def getWorkspaceFile(file_name):
        """
        get the file with the given path 
        """
        return getFile("workspace:/" + file_name)
