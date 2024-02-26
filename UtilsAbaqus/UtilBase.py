class VectorBase():
    def __init__(self, iMin, iMax, deltaI):
        self.MinI = iMin
        self.MaxI = iMax
        self.DeltaI = deltaI
    
    def IsFixDim(self):
        return self.MinI == self.MaxI