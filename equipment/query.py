
from equipment import interface as equipment_interface
from equipment import models as equipment_models
class PlantQuery(equipment_interface.IPlant):
    def get_all_plants(self):
        return equipment_models.Plant.objects.all()


class ScheduleQuery(equipment_interface.ISchedule):
    def get_schedule_by_user(self, user):
        print(f"User to check {user}")
        return equipment_models.Schedule.objects.filter(user=user).values_list("equipment",flat=True)


class EquipmentQuery(equipment_interface.IEquipment):
    def get_equipment_by_id(self, id):
        print(f"id recieve : {id}")
        return equipment_models.Equipment.objects.filter(id__in=id)