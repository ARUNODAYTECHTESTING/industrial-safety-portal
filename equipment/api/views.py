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
from drf_yasg import openapi
from account import models as account_models
from account.api import serializers as account_serializers
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count, Q,Max

from django.db.models import Count, Q, F, ExpressionWrapper, DecimalField
from django.db.models.functions import Coalesce
from rest_framework import generics, permissions
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Q
import logging

logger = logging.getLogger(__name__)
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

class PlantDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,account_permissions.IsPortalAdmin|account_permissions.IsSuperAdmin]
    queryset = equipment_models.Plant.objects.all()
    serializer_class = equipment_serializers.PlantSerializer
    @swagger_auto_schema(
        tags=['Plant'],
        operation_summary="Retrieve a plant",
        operation_description="Get a plant by its ID."
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Plant'],
        operation_summary="Update a plant",
        operation_description="Update an existing plant by its ID."
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Plant'],
        operation_summary="Delete a plant",
        operation_description="Delete a plant by its ID."
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def put(self, request, *args, **kwargs):
        pass

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
        try:
            payload = request.data
            response = super().post(request, *args, **kwargs)
            equipment = equipment_models.Equipment.objects.get(id=response.data['id'])
            audit_parameters = equipment_models.MasterAuditParameter.objects.filter(id__in = payload.get('audit_parameter'))
            if audit_parameters:
                for audit_parameter in audit_parameters:
                    equipment_models.Checkpoint.objects.create(equipment=equipment,audit_parameter = audit_parameter)
            return Response({"message": "Equipment created successfully"},status = status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"message": str(e)}, status = status.HTTP_400_BAD_REQUEST)
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



class ScheduleTypeView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = equipment_serializers.ScheduleTypeSerializer
    queryset = equipment_models.ScheduleType.objects.all()

    @swagger_auto_schema(
        tags=['Schedule'],
        operation_summary="List and create schedule type",
        operation_description="Retrieve a list of schedule type or create new equipment."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Schedule'],
        operation_summary="Create schedule type",
        operation_description="Create new schedule type."
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class ScheduleTypeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = equipment_serializers.ScheduleTypeSerializer
    queryset = equipment_models.ScheduleType.objects.all()

    @swagger_auto_schema(
        tags=['Schedule'],
        operation_summary="Retrieve a schedule",
        operation_description="Get a schedule by its ID."
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Schedule'],
        operation_summary="Update a schedule type",
        operation_description="Update an existing schedule type by its ID."
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Schedule'],
        operation_summary="Delete a schedule type",
        operation_description="Delete a schedule type by its ID."
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ScheduleView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = equipment_serializers.ScheduleSerializer
    queryset = equipment_models.Schedule.objects.all()

    @swagger_auto_schema(
        tags=['Schedule'],
        operation_summary="List and create schedules",
        operation_description="Retrieve a list of schedules or create a new schedule."
    )
    def get(self, request, *args, **kwargs):
        group_names = request.user.groups.values_list('name', flat=True)
        if set(group_names).intersection({"Auditor", "Auditors"}):
            self.queryset = self.queryset.filter(user=request.user)
        else:
            self.queryset = equipment_query.ScheduleQuery().get_schedule_assigned_by(request.user)
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Schedule'],
        operation_summary="Create a schedule",
        operation_description="Create a new schedule with the current user as assigned_by."
    )
    def perform_create(self, serializer):
        serializer.save(assigned_by=self.request.user) 


class ScheduleDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
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
        operation_description="Retrieve a list of checkpoint or create new checkpoint.",
        manual_parameters=[
        openapi.Parameter(
            name='equipment',
            in_='query',
            description='Equipment ID',
            type=openapi.TYPE_INTEGER
        )
    ]
    )
    def get(self, request, *args, **kwargs):
        equipment_id = request.query_params.get('equipment')
        if equipment_id:
            self.queryset = self.queryset.filter(equipment_id=equipment_id)
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['checkpoint'],
        operation_summary="Create checkpoint",
        operation_description="Create new checkpoint."
    )
    def post(self, request, *args, **kwargs):
        try:
            audit_parameter = request.data.get('audit_parameter')
            equipment_id = request.data.get('equipment')
            equipment = equipment_models.Equipment.objects.filter(id=equipment_id).first()
            if not equipment:
                return Response({"error": "Equipment not found"},status = status.HTTP_404_NOT_FOUND)
            audit_parameters = equipment_models.MasterAuditParameter.objects.filter(id__in = audit_parameter)
            if audit_parameters:
                for audit_parameter in audit_parameters:
                    equipment_models.Checkpoint.objects.get_or_create(equipment_id=equipment.id,audit_parameter = audit_parameter)
            return Response({"message": "Checkpoint created successfully"},status = status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": f"{e}"},status = status.HTTP_400_BAD_REQUEST)
    
class CheckPointDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,account_permissions.IsPortalAdmin|account_permissions.IsSuperAdmin|account_permissions.IsAdmin]
    queryset = equipment_models.Checkpoint.objects.all()
    serializer_class = equipment_serializers.CheckPointUpdateSerializer

    @swagger_auto_schema(
        tags=['checkpoint'],
        operation_summary="Retrieve checkpoint",
        operation_description="Get checkpoint by its ID."
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['checkpoint'],
        operation_summary="Update checkpoint",
        operation_description="Update an existing checkpoint by its ID."
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['checkpoint'],
        operation_summary="Delete checkpoint",
        operation_description="Delete checkpoint by its ID."
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ObservationApiView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser]
    queryset = equipment_models.Observation.objects.all()

    serializer_class = equipment_serializers.ObservationSerializer

    @swagger_auto_schema(
        tags=['Observation'],
        operation_summary="List and create observation",
        operation_description="Retrieve a list of observation or create new observation."
    )
    def get(self, request, *args, **kwargs):
        if account_permissions.RoleManager(request.user).is_auditor():
            self.queryset = self.queryset.filter(owner=request.user)
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Observation'],
        operation_summary="Create observation",
        operation_description="Create new observation."
    )
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,department = self.request.user.department) 


class ObservationDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser]
    queryset = equipment_models.Observation.objects.all()
    serializer_class = equipment_serializers.ObservationSerializer

    @swagger_auto_schema(
        tags=['Observation'],
        operation_summary="Retrieve observation",
        operation_description="Get observation by its ID."
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Observation'],
        operation_summary="Update observation",
        operation_description="Update an existing observation by its ID."
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Observation'],
        operation_summary="Delete observation",
        operation_description="Delete observation by its ID."
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



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

class FilterDataView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = None
    serializer_class = None

    @swagger_auto_schema(
        operation_summary="List data associated objects",
        manual_parameters=[
            openapi.Parameter(
                name='plant', 
                in_='query',
                description='Filter by plant ID',
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                name='line', 
                in_='query',
                description='Filter by line ID',
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                name='station', 
                in_='query',
                description='Filter by station ID',
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                name='department', 
                in_='query',
                description='Filter by department ID',
                type=openapi.TYPE_INTEGER
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        try:
            plant = request.GET.get('plant', None)
            line = request.GET.get('line', None)
            station = request.GET.get('station', None)
            department = request.GET.get('department', None)
           
            if plant is not None:
                if request.user.plant:
                    self.queryset = equipment_models.Plant.objects.filter(id=request.user.plant.id)
                    self.serializer_class = equipment_serializers.PlantSerializer
                else:
                    
                    self.queryset = equipment_models.Plant.objects.filter(id=plant)
                    self.serializer_class = equipment_serializers.PlantSerializer
            
            elif department is not None:
                if request.user.department:
                    self.queryset = account_models.Department.objects.filter(id=request.user.department.id)
                    self.serializer_class = account_serializers.DepartmentSerializer
                else:
                    self.queryset = account_models.Department.objects.filter(id=department)
                    self.serializer_class = account_serializers.DepartmentSerializer
            
            elif line is not None:
                    self.queryset = equipment_models.Station.objects.filter(line_id=line)
                    self.serializer_class = equipment_serializers.StationSerializer

            elif station is not None:
                self.queryset = equipment_models.Station.objects.filter(id=station)
                self.serializer_class = equipment_serializers.StationSerializer
            
            elif account_permissions.RoleManager(request.user).is_auditor():
                return Response({"status":400,"data":"Please select plant,department to know Auditors plants,departments"},status=400)
            else:
                user_type = account_query.GroupQuery().get_user_type_level(request.user)
                user_type_ids = [ut['id'] for ut in user_type]
                self.queryset = account_models.User.objects.filter(groups__id__in=user_type_ids,manage_by = request.user)
                self.serializer_class = account_serializers.UserSerializer
              
            return super().get(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)







class AuditSummary(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = equipment_models.Observation.objects.all()
    serializer_class = equipment_serializers.ObservationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'request_status', 
        'approve_status',
    ]

    @swagger_auto_schema(
        tags=['Audit'],
        operation_summary="Comprehensive Audit Overview",
        operation_description="Retrieve detailed audit statistics including total audits, compliance score, and status breakdown"
    )
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # Apply any filters from the request
        group_names = request.user.groups.values_list('name', flat=True)
        if set(group_names).intersection({"Auditor", "Auditors"}):
            queryset = queryset.filter(owner=request.user)
        else:
            user_id = equipment_query.ScheduleQuery().get_schedule_assigned_by(request.user).values_list("user_id",flat=True)
            queryset = queryset.filter(owner__in=user_id)

        # Total Audits Completed
        total_audits = queryset.filter().count()
        
        # Pending Audits
        pending_audits = queryset.filter(request_status='open').count()
        
        # Compliance Score Calculation
        total_observations = queryset.count()
        approved_observations = queryset.filter(approve_status='approved').count()
        compliance_score = (approved_observations / total_observations * 100) if total_observations > 0 else 0
        
        # Detailed Status Breakdown
        status_breakdown = {
            'pending': queryset.filter(request_status='open').count(),
            'ongoing': queryset.filter(request_status='resolved').count(),
            'complete': queryset.filter(request_status='closed').count(),
            # 'failed': queryset.filter(request_status='failed').count()
        }
        
        # Pass vs Fail Breakdown
        pass_fail_breakdown = {
            'passed': queryset.filter(approve_status='approved').count(),
            'rejected': queryset.filter(approve_status='rejected').count(),
            'pending_review': queryset.filter(approve_status='pending').count()
        }
        
      
       
        
        return Response({
            'summary_cards': {
                'total_audits': total_audits,
                'pending_audits': pending_audits,
                'compliance_score': round(compliance_score, 2),
                'pass_fail_ratio': pass_fail_breakdown
            },
            'status_breakdown': status_breakdown,
           
        })

class NotificationSummary(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = equipment_models.Observation.objects.all()
    serializer_class = equipment_serializers.ObservationSerializer

    def get_filtered_queryset(self, user, base_queryset):
        """Helper method to get filtered queryset based on user role"""
        if not user or not base_queryset:
            logger.warning("User or base_queryset is None")
            return []

        common_values = [
            "id",
            "checkpoint__equipment__name",
            "updated_at",
            "request_status",
            "owner__name",
            "remark",
            "owner__schedule__assigned_by__name",
        ]

        try:
            # Filter out completed requests
            filtered_queryset = base_queryset.exclude(request_status="complete")
            
            # Get user groups
            user_groups = set(user.groups.values_list('name', flat=True))
            
            # Check if user is an auditor
            if "Auditor" in user_groups or "Auditors" in user_groups:
                if user.last_login is None:
                    logger.warning(f"User {user.id} has no last_login timestamp")
                    return filtered_queryset.filter(
                        owner=user
                    ).values(*common_values)
                    
                return filtered_queryset.filter(
                    owner=user,
                    updated_at__gt=user.last_login
                ).values(*common_values)

            # For non-auditors
            schedule_query = equipment_query.ScheduleQuery()
            assigned_users = schedule_query.get_schedule_assigned_by(user)
            
            if assigned_users is None:
                logger.warning(f"No assigned users found for user {user.id}")
                return []
                
            user_ids = assigned_users.values_list("user_id", flat=True)
            
            if not user_ids:
                logger.warning(f"Empty user_ids list for user {user.id}")
                return []
                
            return filtered_queryset.filter(
                owner__in=list(user_ids)
            ).values(*common_values)

        except Exception as e:
            logger.error(f"Error in get_filtered_queryset: {str(e)}")
            return []

    @swagger_auto_schema(
        tags=['Audit'],
        operation_summary="Comprehensive Audit Overview",
        operation_description="Retrieve detailed audit statistics including total audits, compliance score, and status breakdown"
    )
    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_filtered_queryset(request.user, self.get_queryset())
            return Response({
                "status": 200,
                "data": list(queryset)  # Explicitly convert to list
            },status=200)
        except Exception as e:
            logger.error(f"Error in get method: {str(e)}")
            return Response({
                "status": 500,
                "error": "An error occurred while processing your request",
                "detail": str(e)
            }, status=500)

class AuditorAuditSummary(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = account_models.User.objects.filter(observations__isnull=False).distinct()
    
    @swagger_auto_schema(
        tags=['Audit'],
        operation_summary="Comprehensive Auditor Performance Tracking",
        operation_description="Detailed analytics of auditor performance including audit status breakdown and compliance scores"
    )
    def get(self, request, *args, **kwargs):
        # Comprehensive Auditor Performance Tracking
        auditor_performance = self.queryset.annotate(
            # Audit Counts
            total_audits=Count('observations', distinct=True),
            completed_audits=Count('observations', filter=Q(observations__request_status='closed'), distinct=True),
            pending_audits=Count('observations', filter=Q(observations__request_status='open'), distinct=True),
            ongoing_audits=Count('observations', filter=Q(observations__request_status='resolved'), distinct=True),
            # failed_audits=Count('observations', filter=Q(observations__request_status='failed'), distinct=True),
            
            # Approval Status Counts
            approved_audits=Count('observations', filter=Q(observations__approve_status='approved'), distinct=True),
            rejected_audits=Count('observations', filter=Q(observations__approve_status='rejected'), distinct=True),
            
            # Audit Performance Metrics
            compliance_score=ExpressionWrapper(
                Coalesce(
                    Count('observations', filter=Q(observations__approve_status='approved'), distinct=True) * 100.0 / 
                    Coalesce(Count('observations', distinct=True), 1),
                    0
                ),
                output_field=DecimalField(max_digits=5, decimal_places=2)
            )
        ).values(
            'id', 
            'name',
            'email',
            'total_audits',
            'completed_audits',
            'pending_audits',
            'ongoing_audits',
            # 'failed_audits',
            'approved_audits',
            'rejected_audits',
            'compliance_score'
        ).order_by('-total_audits')
        
        # Prepare Detailed Performance List
        auditor_performance_list = []
        # overall_performance_summary = {
        #     'total_auditors': 0,
        #     'total_audits': 0,
        #     'average_compliance_score': 0,
        #     'status_breakdown': {
        #         'completed': 0,
        #         'pending': 0,
        #         'ongoing': 0,
        #         'failed': 0
        #     }
        # }
        
        for auditor in auditor_performance:
            # Calculate detailed performance metrics
            auditor_data = {
                'auditor_id': auditor['id'],
                'name': auditor['name'],
                'email': auditor['email'],
                
                # Audit Status Breakdown
                'audit_status_breakdown': {
                    'total': auditor['total_audits'],
                    'completed': auditor['completed_audits'],
                    'pending': auditor['pending_audits'],
                    'ongoing': auditor['ongoing_audits'],
                    # 'failed': auditor['failed_audits']
                },
                
                # Approval Status Details
                'approval_status': {
                    'approved': auditor['approved_audits'],
                    'rejected': auditor['rejected_audits']
                },
                
                # Compliance Score
                'compliance_score': float(auditor['compliance_score']),
                
                # Performance Indicators
                'performance_indicators': {
                    'approval_rate': round(
                        (auditor['approved_audits'] / auditor['total_audits'] * 100) 
                        if auditor['total_audits'] > 0 else 0, 
                        2
                    ),
                    'rejection_rate': round(
                        (auditor['rejected_audits'] / auditor['total_audits'] * 100) 
                        if auditor['total_audits'] > 0 else 0, 
                        2
                    )
                }
            }
            
            # # Update Overall Performance Summary
            # overall_performance_summary['total_auditors'] += 1
            # overall_performance_summary['total_audits'] += auditor_data['audit_status_breakdown']['total']
            # overall_performance_summary['average_compliance_score'] += auditor_data['compliance_score']
            
            # # Update Status Breakdown
            # overall_performance_summary['status_breakdown']['completed'] += auditor_data['audit_status_breakdown']['completed']
            # overall_performance_summary['status_breakdown']['pending'] += auditor_data['audit_status_breakdown']['pending']
            # overall_performance_summary['status_breakdown']['ongoing'] += auditor_data['audit_status_breakdown']['ongoing']
            # overall_performance_summary['status_breakdown']['failed'] += auditor_data['audit_status_breakdown']['failed']
            
            auditor_performance_list.append(auditor_data)
        
        # Calculate average compliance score
        # if overall_performance_summary['total_auditors'] > 0:
        #     overall_performance_summary['average_compliance_score'] = round(
        #         overall_performance_summary['average_compliance_score'] / overall_performance_summary['total_auditors'], 
        #         2
        #     )
        
        return Response({
            'auditors': auditor_performance_list,
            # 'overall_performance_summary': overall_performance_summary
        })
    

