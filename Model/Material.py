import uuid

class Material():
    # Id: id of material (UUID) - adm
    # E : Elastic Module (int) - MPa
    # P : poisson coef (int) - adm
    def __init__(self, baseId, e, p):
        self.BaseId = baseId
        self.E = e
        self.P = u