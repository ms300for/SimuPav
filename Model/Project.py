class Project():
    def __init__(self, materialsBase, pavLayerBases, airPlaneCharge, models):
        self.MaterialsBase = materialsBase
        self.PavLayersBase = pavLayerBases
        self.AirPlaneCharge = airPlaneCharge
        
        self.Models = models
        
        self.HasGenerateModels = len(self.Models) > 0