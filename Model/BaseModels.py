#--------------------------------------------------------------------------------------------------#
class ModelBase():
    def __init__(self, id):
        self.ModelId = id
        
    def GetId(self):
        return self.Id
    
    def IsSameValue(self, value1, value2):
        return value1 == value2
    
    def GetInterval(self, valueMin, valueMax, step):
        print(valueMin, valueMax, step)
        if self.IsSameValue(valueMin, valueMax):
            return [valueMin]
        
        iterationQuant = (valueMax - valueMin)/step
        print(iterationQuant)
        if (round(iterationQuant, ndigits=5) == int(iterationQuant)):
            return [round(valueMin + e*step, ndigits=5) for e in range(0, int(iterationQuant) + 1, 1)]
        else:
            return [round(valueMin + e*step, ndigits=5) for e in range(0, int(iterationQuant) + 1, 1)] + [valueMax]

#--------------------------------------------------------------------------------------------------#
class MaterialBase(ModelBase):
    # Id: id of material (UUID) - adm
    # E : Elastic Module (int) - MPa
    # P : poisson coef (int) - adm
    #-------------------------------
    # Vector = [min, max, step]
    def __init__(self, idMaterial, name, elasticModule, poisson):
        super().__init__(idMaterial)
        
        self.Name = name 
        self.ElasticModule = elasticModule
        self.Poisson = poisson
        
    def GetIntervalE(self):
        return self.GetInterval(self.ElasticModule.MinI, self.ElasticModule.MaxI, self.ElasticModule.DeltaI)
        
    def GetIntervalP(self):
        return self.GetInterval(self.Poisson.MinI, self.Poisson.MaxI, self.Poisson.DeltaI)

#--------------------------------------------------------------------------------------------------#
class PavLayerBase(ModelBase):
    def __init__(self, layerId, name, xSize, ySize, zSize):
        super().__init__(layerId)
        
        self.Name = name
        self.XSize = xSize
        self.YSize = ySize
        self.ZSize = zSize
    
    def GetIntervalX(self):
        return self.GetInterval(self.XSize.MinI, self.XSize.MaxI, self.XSize.DeltaI)
    
    def GetIntervalY(self):
        return self.GetInterval(self.YSize.MinI, self.YSize.MaxI, self.YSize.DeltaI)
    
    def GetIntervalZ(self):
        return self.GetInterval(self.ZSize.MinI, self.ZSize.MaxI, self.ZSize.DeltaI)