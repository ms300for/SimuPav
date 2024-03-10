from PavLayer import PavLayer
class SimulationModel():
    def __init__(self, pav_layers: PavLayer, step: float, sensores: VectorBase) -> None:
        self.pav_layers = pav_layers
        self.sensores = sensores
        self.step = step
 
    def calc_size(self, dim):
        pass
