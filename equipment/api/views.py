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
from rest_framework.views import APIView
from equipment import query as equipment_query
from account import query as account_query
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,HTTP_201_CREATED)

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
    permission_classes = [permissions.IsAuthenticated,account_permissions.IsPortalAdmin|account_permissions.IsSuperAdmin]

    queryset = equipment_models.EquipmentType.objects.all()
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
    # parser_classes = [MultiPartParser]
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
        payload = request.data
        response = super().post(request, *args, **kwargs)
        equipment = equipment_models.Equipment.objects.get(id=response.data['id'])
        audit_parameters = equipment_models.MasterAuditParameter.objects.filter(id__in = payload.get('audit_parameter'))
        if audit_parameters:
            for audit_parameter in audit_parameters:
                equipment_models.Checkpoint.objects.create(equipment=equipment,audit_parameter = audit_parameter)
        return Response({"message": "Equipment created successfully"},status = status.HTTP_201_CREATED)


class EquipmentDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,account_permissions.IsPortalAdmin|account_permissions.IsSuperAdmin|account_permissions.IsAdmin]

    # parser_classes = [MultiPartParser]
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


class MasterAuditParameter(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,account_permissions.IsPortalAdmin|account_permissions.IsSuperAdmin|account_permissions.IsAdmin]
    queryset = equipment_models.MasterAuditParameter.objects.all()
    serializer_class = equipment_serializers.MasterAuditParameterSerializer

    @swagger_auto_schema(
        tags=['MasterAuditParameters'],
        operation_summary="List and create Audit Parameters",
        operation_description="Retrieve a list of Audit Parameters or create new Audit Parameters."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['MasterAuditParameters'],
        operation_summary="Create Audit Parameters",
        operation_description="Create new Audit Parameters."
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class MasterAuditParameterDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,account_permissions.IsPortalAdmin|account_permissions.IsSuperAdmin|account_permissions.IsAdmin]
    queryset = equipment_models.MasterAuditParameter.objects.all()
    serializer_class = equipment_serializers.MasterAuditParameterSerializer

    @swagger_auto_schema(
        tags=['MasterAuditParameters'],
        operation_summary="Retrieve Audit Parameters",
        operation_description="Get Audit Parameters by its ID."
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['MasterAuditParameters'],
        operation_summary="Update Audit Parameters",
        operation_description="Update an existing Audit Parameters by its ID."
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['MasterAuditParameters'],
        operation_summary="Delete Audit Parameters",
        operation_description="Delete Audit Parameters by its ID."
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def put(self, request, *args, **kwargs):
        pass



class CheckPointView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,account_permissions.IsPortalAdmin|account_permissions.IsSuperAdmin|account_permissions.IsAdmin]
    # parser_classes = [MultiPartParser]
    queryset = equipment_models.Checkpoint.objects.all()
    serializer_class = equipment_serializers.CheckPointSerializer

    @swagger_auto_schema(
        tags=['checkpoint'],
        operation_summary="List and create checkpoint",
        operation_description="Retrieve a list of checkpoint or create new checkpoint."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['checkpoint'],
        operation_summary="Create checkpoint",
        operation_description="Create new checkpoint."
    )
    def post(self, request, *args, **kwargs):
        try:
            audit_parameter = request.data.get('audit_parameter')
            equipment = request.data.get('equipment')
            audit_parameters = equipment_models.MasterAuditParameter.objects.filter(id__in = audit_parameter)
            if audit_parameters:
                for audit_parameter in audit_parameters:
                    equipment_models.Checkpoint.objects.get_or_create(equipment_id=equipment,audit_parameter = audit_parameter)
            return Response({"message": "Checkpoint created successfully"},status = status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": f"{e}"},status = status.HTTP_400_BAD_REQUEST)
    

class ObservationApiView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,account_permissions.IsAuditor]
    parser_classes = [MultiPartParser]
    queryset = equipment_models.Observation.objects.all()
    serializer_class = equipment_serializers.ObservationSerializer

    @swagger_auto_schema(
        tags=['Observation'],
        operation_summary="List and create observation",
        operation_description="Retrieve a list of observation or create new observation."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Observation'],
        operation_summary="Create observation",
        operation_description="Create new observation."
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ListPlantUserTypeDepartmentView(APIView):
    @swagger_auto_schema(
        tags=['ListPlantUserTypeDepartment'],
        operation_summary="List all plant department and users type",
        operation_description="List all plant department and users type"
    )
    def get(self, request, *args, **kwargs):
        try:
            plant = equipment_query.PlantQuery().get_all_plants().values("id","name")
            department = account_query.DepartmentRepository().get_all_departments().values("id","name")
            user_typt = account_query.GroupQuery().get_user_type_level(user=request.user)
            return Response({"status":200,"data":{"plant":plant,"department": department,"user_typt": user_typt}},status=HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)