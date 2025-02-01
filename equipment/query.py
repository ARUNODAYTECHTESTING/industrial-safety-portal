
from equipment import interface as equipment_interface
from equipment import models as equipment_models
class PlantQuery(equipment_interface.IPlant):
    def get_all_plants(self):
        return equipment_models.Plant.objects.all()