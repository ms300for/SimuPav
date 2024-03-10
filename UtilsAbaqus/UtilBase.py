class VectorBase():
    def __init__(self, iMin, iMax, deltaI):
        self.MinI = iMin
        self.MaxI = iMax
        self.DeltaI = deltaI
    
    def IsFixDim(self):
        return self.MinI == self.MaxI
    
class VectorArea():
    def __init__(self, len_x: float, len_y: float, reference_x: float = 0, reference_y: float = 0):
        self.len_x = len_x
        self.len_y = len_y
        self.ref_x = reference_x
        self.ref_y = reference_y
        
    def get_area(self):
        return self.len_x*self.len_y