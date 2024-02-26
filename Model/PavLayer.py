
class PavLayer():
    def __init__(self, baseId, xSize, ySize, zSize):
        self.XSize = xSize
        self.YSize = ySize
        self.ZSize = zSize
        
        self.BaseId = baseId
        self.Material = None
        self.LoadCharge = []
        
    def IsValid(self):
        if self.Material == None:
            return False
        return True
    
    def SetMaterial(self, material):
        self.Material = material