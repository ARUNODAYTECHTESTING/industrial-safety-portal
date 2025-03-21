
from equipment import interface as equipment_interface
from equipment import models as equipment_models
from django.db.models import Q

class PlantQuery(equipment_interface.IPlant):
    def get_all_plants(self):
        return equipment_models.Plant.objects.all()


class ScheduleQuery(equipment_interface.ISchedule):
    def get_schedule_by_user(self, user):
        return equipment_models.Schedule.objects.filter(user=user).values_list("equipment",flat=True)
    def get_schedule_by_user_list(self, user_list):
        return equipment_models.Schedule.objects.filter(user_id__in=user_list)
    def get_schedule_assigned_by(self, assigner):
        return equipment_models.Schedule.objects.filter(assigned_by=assigner)

    def get_schedule_by_equipment(self, equipment_id, user_id):
        return equipment_models.Schedule.objects.filter(
        equipment_id=equipment_id,
        user_id=user_id,
        ).first()
    def get_schedule_by_assigner_or_auditor(self, assigner_or_auditor):
        return equipment_models.Schedule.objects.filter(Q(assigned_by=assigner_or_auditor)|Q(user=assigner_or_auditor))

class EquipmentQuery(equipment_interface.IEquipment):
    def get_equipment_by_id(self, id):
        return equipment_models.Equipment.objects.filter(id__in=list(id))
    
    def get_object(self, id):
        return equipment_models.Equipment.objects.filter(id=id).first()


class CheckPointQuery(equipment_interface.ICheckPoint):
    def get_object(self, id):
        return equipment_models.Checkpoint.objects.filter(id=id).first()
    
class AuditQuery(equipment_interface.IAudit):
    def get_audits_by_equipment_id(self, id):
        return equipment_models.Audit.objects.filter(equipment_id=id)