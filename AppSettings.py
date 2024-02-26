import json
import os
from Service.ProjectService import ProjectService

defaultDataPath = "\\DefaultData\\Dataset\\"
class AppSettings():
    def __init__(self):
        self.HasChargeProject = False
        self.Settings = {"ActualDataSetPath": "", 
                         "ActualChargePath" : os.path.abspath(os.getcwd()) + "\\"}
        self.ReadSettings()
        if (len(self.Settings["ActualDataSetPath"]) == 0):
            print("Sem projeto definido!")
        else:
            self.HasChargeProject = True
            
        self.LoadService()
    
    def LoadService(self):
        self.ProjectService = ProjectService()
    
    def SaveSettings(self):
        with open("AppSettings.json", "w") as outFile:
            outFile.write(json.dumps(self.Settings, indent=4))
    
    def ReadSettings(self):
        try:
            with open("AppSettings.json", "r") as inputFile:
                self.Settings = json.load(inputFile)
        except:
            self.SaveSettings()
            
                