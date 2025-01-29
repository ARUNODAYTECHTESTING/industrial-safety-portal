from django.urls import path
from equipment.api import views as equipment_views
urlpatterns = [
    path("plant/",equipment_views.PlantView.as_view(),name = 'plant'),
    path("equipment-type/",equipment_views.EquipmentTypeView.as_view(),name = 'equipment-type'),
    path("equipment-type-details/<int:pk>/",equipment_views.EquipmentTypeDetailsView.as_view(),name = 'equipment-type-details'),
    path("line/",equipment_views.LineView.as_view(),name = 'line'),
    path("line-details/",equipment_views.LineDetailsView.as_view(),name = 'line-details'),
    path("station/",equipment_views.StationView.as_view(),name = 'station'),
    path("station-details/<int:pk>/",equipment_views.StationDetailsView.as_view(),name = 'station-details'),
    path("equipment/",equipment_views.EquipmentView.as_view(),name = 'equipment'),
    path("equipment-details/<int:pk>/",equipment_views.EquipmentDetailsView.as_view(),name = 'equipment-details'),
    path("checklist/",equipment_views.CheckListView.as_view(),name = 'checklist'),
    path("checklist-details/<int:pk>/",equipment_views.CheckListDetailsView.as_view(),name = 'checklist-details'),
    path("schedule/",equipment_views.ScheduleView.as_view(),name = 'schedule'),
    path("schedule-details/<int:pk>/",equipment_views.ScheduleDetailsView.as_view(),name = 'schedule-details'),
]