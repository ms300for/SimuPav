
class PavLayer():
    def __init__(self, baseId, xSize, ySize, zSize, name):
        self.x_size = xSize
        self.y_size = ySize
        self.z_size = zSize
        
        self.base_id = baseId
        self.material = None
        self.load_charge = []
        
        self.name = name
        
    def is_valid(self):
        if self.Material == None:
            return False
        return True
    
    def set_material(self, material):
        self.Material = material