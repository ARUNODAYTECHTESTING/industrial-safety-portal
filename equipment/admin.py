from django.contrib import admin
from equipment import models as equipment_models
# Register your models here.
admin.site.register(equipment_models.Equipment)
admin.site.register(equipment_models.EquipmentType)
admin.site.register(equipment_models.Plant)
admin.site.register(equipment_models.Line)
admin.site.register(equipment_models.Station)
admin.site.register(equipment_models.ScheduleType)
admin.site.register(equipment_models.Schedule)
admin.site.register(equipment_models.Observation)
