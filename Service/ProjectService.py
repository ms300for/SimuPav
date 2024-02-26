from UtilsAbaqus.UtilsList import *
from UtilsAbaqus.UtilBase import *
from Service.BaseService import BaseService
from View.Formulary import *

class ProjectService(BaseService):
    def __init__(self):
        super().__init__()
              
    def OpenProject(self, projectPath):
        pass
    
    def WriteProject(self, projectPath, project):
        pass
        
    def CreateProject(self, root):
        CreateProjectFormulary(root)
        