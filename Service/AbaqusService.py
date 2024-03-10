from UtilsAbaqus.UtilBase import VectorArea

from Model.Material import Material
from Model.PavLayer import PavLayer
from Model.Charge import Charge
from Model.Project import Project
from Model.SimulationModel import SimulationModel

pav_layer_list = [PavLayer(1, 3.5, 7, 10.00, "Subleito"), 
                  PavLayer(2, 3.5, 7, 0.40, "Subbase"),
                  PavLayer(3, 3.5, 7, 0.30, "Base"),
                  PavLayer(4, 3.5, 7, 0.20, "Revestimento")]
chargeTest = Charge("A320", 20, VectorArea(0.504, 0.315, 0, 0))
material_list = [Material(1, 150,0.4), 
                 Material(2, 200,0.35),
                 Material(3, 170,0.35),
                 Material(4, 2000,0.3)]
print(chargeTest.get_area())