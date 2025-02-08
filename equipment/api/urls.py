from django.urls import path,include
from equipment.api import views as equipment_views


urlpatterns = [
    path("master-audit-parameter/",equipment_views.MasterAuditParameter.as_view(),name = 'master-audit-parameter'),
    path("master-audit-parameter-details/<int:pk>/",equipment_views.MasterAuditParameterDetails.as_view(),name = 'master-audit-parameter-details'),
    path("checkpoint/",equipment_views.CheckPointView.as_view(),name = 'checkpoint'),
    path("checkpoint-details/<int:pk>/",equipment_views.CheckPointDetailsView.as_view(),name = 'checkpoint-details'),
    path("plant/",equipment_views.PlantView.as_view(),name = 'plant'),
    path("plant-details/<int:pk>/",equipment_views.PlantDetailsView.as_view(),name = 'plant-details'),
    path("observation/",equipment_views.ObservationApiView.as_view(),name = 'observation'),
    path("observation-details/<int:pk>/",equipment_views.ObservationDetailsApiView.as_view(),name = 'observation-details'),
    path("equipment-type/",equipment_views.EquipmentTypeView.as_view(),name = 'equipment-type'),
    path("equipment-type-details/<int:pk>/",equipment_views.EquipmentTypeDetailsView.as_view(),name = 'equipment-type-details'),
    path("line/",equipment_views.LineView.as_view(),name = 'line'),
    path("line-details/<int:pk>/",equipment_views.LineDetailsView.as_view(),name = 'line-details'),
    path("station/",equipment_views.StationView.as_view(),name = 'station'),
    path("station-details/<int:pk>/",equipment_views.StationDetailsView.as_view(),name = 'station-details'),
    path("",equipment_views.EquipmentView.as_view(),name = 'equipment'),
    path("equipment-details/<int:pk>/",equipment_views.EquipmentDetailsView.as_view(),name = 'equipment-details'),
    path("schedule/",equipment_views.ScheduleView.as_view(),name = 'schedule'),
    path("schedule-details/<int:pk>/",equipment_views.ScheduleDetailsView.as_view(),name = 'schedule-details'),
    path("schedule-type/",equipment_views.ScheduleTypeView.as_view(),name = 'schedule-type'),
    path("schedule-type-details/<int:pk>/",equipment_views.ScheduleTypeDetailsView.as_view(),name = 'schedule-type-details'),
    path("plant-user-type-department/",equipment_views.ListPlantUserTypeDepartmentView.as_view(),name = 'plant-user-type-department'),
    path("filter-data/",equipment_views.FilterDataView.as_view(),name = 'filter-data'),
    path("audit-summery/",equipment_views.AuditSummary.as_view(),name = 'audit-summery'),
    path("auditor-summery/",equipment_views.AuditorAuditSummary.as_view(),name = 'auditor-summery'),
    path("notification/",equipment_views.NotificationView.as_view(),name = 'notification'),





]
