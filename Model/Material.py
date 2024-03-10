import uuid

class Material():
    # Id: id of material (UUID) - adm
    # E : Elastic Module (int) - MPa
    # P : poisson coef (int) - adm
    def __init__(self, baseId, e, p):
        self.base_id = baseId
        self.E = e
        self.P = u