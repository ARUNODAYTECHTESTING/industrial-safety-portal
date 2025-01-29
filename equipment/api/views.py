from rest_framework import generics,status
from equipment import models as equipment_models
from equipment.api import serializers as equipment_serializers
from rest_framework.parsers import MultiPartParser
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.mixins import UserPassesTestMixin
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from account import permissions as account_permissions

class EquipmentTypeView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,account_permissions.IsPortalAdmin|account_permissions.IsSuperAdmin]

    queryset = equipment_models.EquipmentType.objects.all()
    serializer_class = equipment_serializers.EquipmentTypeSerializer

    @swagger_auto_schema(
        tags=['EquipmentType'],
        operation_summary="List and create equipment types",
        operation_description="Retrieve a list of equipment types or create a new equipment type."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['EquipmentType'],
        operation_summary="Create an equipment type",
        operation_description="Create a new equipment type."
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def put(self, request, *args, **kwargs):
        pass

class EquipmentTypeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = equipment_models.Equipment.objects.all()
    serializer_class = equipment_serializers.EquipmentTypeSerializer

    @swagger_auto_schema(
        tags=['EquipmentType'],
        operation_summary="Retrieve an equipment type",
        operation_description="Get an equipment type by its ID."
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['EquipmentType'],
        operation_summary="Update an equipment type",
        operation_description="Update an existing equipment type by its ID."
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['EquipmentType'],
        operation_summary="Delete an equipment type",
        operation_description="Delete an equipment type by its ID."
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def put(self, request, *args, **kwargs):
        pass

class PlantView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,account_permissions.IsPortalAdmin,]
    queryset = equipment_models.Plant.objects.all()
    serializer_class = equipment_serializers.PlantSerializer
    
    
    @swagger_auto_schema(
        tags=['Plant'],
        operation_summary="List and create plants",
        operation_description="Retrieve a list of plants or create a new plant."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Plant'],
        operation_summary="Create a plant",
        operation_description="Create a new plant."
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    

class LineView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,account_permissions.IsPortalAdmin|account_permissions.IsSuperAdmin]
    queryset = equipment_models.Line.objects.all()
    serializer_class = equipment_serializers.LineSerializer

    @swagger_auto_schema(
        tags=['Line'],
        operation_summary="List and create lines",
        operation_description="Retrieve a list of lines or create a new line."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Line'],
        operation_summary="Create a line",
        operation_description="Create a new line."
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class LineDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,account_permissions.IsPortalAdmin|account_permissions.IsSuperAdmin]
    queryset = equipment_models.Line.objects.all()
    serializer_class = equipment_serializers.LineSerializer

    @swagger_auto_schema(
        tags=['Line'],
        operation_summary="Retrieve a line",
        operation_description="Get a line by its ID."
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Line'],
        operation_summary="Update a line",
        operation_description="Update an existing line by its ID."
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Line'],
        operation_summary="Delete a line",
        operation_description="Delete a line by its ID."
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def put(self, request, *args, **kwargs):
        pass

class StationView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,account_permissions.IsPortalAdmin|account_permissions.IsSuperAdmin]
    queryset = equipment_models.Station.objects.all()
    serializer_class = equipment_serializers.StationSerializer

    @swagger_auto_schema(
        tags=['Station'],
        operation_summary="List and create stations",
        operation_description="Retrieve a list of stations or create a new station."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Station'],
        operation_summary="Create a station",
        operation_description="Create a new station."
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    

class StationDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,account_permissions.IsPortalAdmin|account_permissions.IsSuperAdmin]
    queryset = equipment_models.Station.objects.all()
    serializer_class = equipment_serializers.StationSerializer

    @swagger_auto_schema(
        tags=['Station'],
        operation_summary="Retrieve a station",
        operation_description="Get a station by its ID."
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Station'],
        operation_summary="Update a station",
        operation_description="Update an existing station by its ID."
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Station'],
        operation_summary="Delete a station",
        operation_description="Delete a station by its ID."
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def put(self, request, *args, **kwargs):
        pass

class EquipmentView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,account_permissions.IsPortalAdmin|account_permissions.IsSuperAdmin|account_permissions.IsAdmin]
    parser_classes = [MultiPartParser]
    queryset = equipment_models.Equipment.objects.all()
    serializer_class = equipment_serializers.EquipmentSerializer

    @swagger_auto_schema(
        tags=['Equipment'],
        operation_summary="List and create equipment",
        operation_description="Retrieve a list of equipment or create new equipment."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Equipment'],
        operation_summary="Create equipment",
        operation_description="Create new equipment."
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class EquipmentDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,account_permissions.IsPortalAdmin|account_permissions.IsSuperAdmin|account_permissions.IsAdmin]

    parser_classes = [MultiPartParser]
    queryset = equipment_models.Equipment.objects.all()
    serializer_class = equipment_serializers.EquipmentSerializer

    @swagger_auto_schema(
        tags=['Equipment'],
        operation_summary="Retrieve equipment",
        operation_description="Get equipment by its ID."
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Equipment'],
        operation_summary="Update equipment",
        operation_description="Update an existing equipment by its ID."
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Equipment'],
        operation_summary="Delete equipment",
        operation_description="Delete equipment by its ID."
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def put(self, request, *args, **kwargs):
        pass


class ScheduleView(generics.ListCreateAPIView):
    serializer_class = equipment_serializers.ScheduleSerializer
    queryset = equipment_models.Schedule.objects.all()

    @swagger_auto_schema(
        tags=['Schedule'],
        operation_summary="List and create schedules",
        operation_description="Retrieve a list of schedules or create a new schedule."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Schedule'],
        operation_summary="Create a schedule",
        operation_description="Create a new schedule."
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ScheduleDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = equipment_serializers.ScheduleSerializer
    queryset = equipment_models.Schedule.objects.all()

    @swagger_auto_schema(
        tags=['Schedule'],
        operation_summary="Retrieve a schedule",
        operation_description="Get a schedule by its ID."
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Schedule'],
        operation_summary="Update a schedule",
        operation_description="Update an existing schedule by its ID."
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Schedule'],
        operation_summary="Delete a schedule",
        operation_description="Delete a schedule by its ID."
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    @swagger_auto_schema(auto_schema=None)
    def put(self, request, *args, **kwargs):
        pass