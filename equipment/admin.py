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
admin.site.register(equipment_models.MasterAuditParameter)
admin.site.register(equipment_models.Checkpoint)



class ObservationAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'checkpoint', 'category', 'request_status', 'approve_status',
        'owner', 'department', 'plant', 'target_date', 'actual_complete_date',
        'created_at', 'updated_at'
    )
    list_filter = ('request_status', 'approve_status', 'department', 'plant')
    search_fields = ('name', 'remark', 'corrective_remark')
    ordering = ('-created_at',)

admin.site.register(equipment_models.Observation,ObservationAdmin)

