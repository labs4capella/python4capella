# this script define some utility methods to interact with the Capella platform
from typing import Any, List

def getSelection():
    pass
def getProject(name):
    pass
def refreshResource(folder):
    pass
def getFile(file_name):
    pass


# includes needed to interact with the Eclipse platform
loadModule('/System/UI')
loadModule('/System/Resources')

include('../java_api/Sirius_API.py')
if False:
    from java_api.Sirius_API import *

class CapellaPlatform():
    @staticmethod
    def getFirstSelectedElement() -> Any:
        """
        return the first element select by the user (if several are selected)
        """
        return getSelection().getFirstElement()
    
    @staticmethod
    def getSelectedElements() -> List[Any]:
        """
        return the list of selected elements
        """
        return getSelection().toList()
    
    @staticmethod
    def getModelPath(elem : Any) -> str:
        """
        return the relative path toward the aird file of a CapellaElement or Diagram
        """
        res = Sirius.get_session(elem.get_java_object()).getSessionResource().getURI().toPlatformString(True)
        res = res[1:res.rfind(".")] + ".aird"
        return res
    
    @staticmethod
    def getProject(name: str) -> Any:
        """
        retrieve a project defined in the Project Explorer from its name
        """
        return getProject(name)
    
    @staticmethod
    def getFolder(project: Any, folder_name: str) -> Any:
        """
        retrieve or create a folder in a project from its name
        """
        folder = project.getFolder(folder_name)
        if not folder.exists():
            folder.create(True, True, None)
        return folder
    
    @staticmethod
    def getAbsolutePath(folder: Any) -> str:
        """
        get the absolute path of a folder
        """
        return folder.getLocation().toString()
    
    @staticmethod
    def refresh(folder: Any):
        """
        refresh the content of a folder in the Project Explorer
        """
        refreshResource(folder)
    
    @staticmethod
    def getWorkspaceFile(file_name: str) -> Any:
        """
        get the file with the given path 
        """
        return getFile("workspace:/" + file_name)
