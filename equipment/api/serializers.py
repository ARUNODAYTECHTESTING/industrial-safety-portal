from rest_framework import serializers
from equipment import models as equipment_models
from account.api import serializers as account_api_serializers
from django.utils import timezone

class EquipmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = equipment_models.EquipmentType
        fields = ['id', 'name']

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = equipment_models.Plant
        fields = ['id', 'name']


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = equipment_models.Line
        fields = ['id', 'name','plant']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['plant'] = PlantSerializer(instance.plant).data
        return representation
 
   
class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = equipment_models.Station
        fields = ['id', 'name','plant','line']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['plant'] = PlantSerializer(instance.plant).data
        line_serializer = LineSerializer(instance.line).data
        representation['line'] = {'id':line_serializer.get('id'),'name':line_serializer.get('name')}
        return representation


    
    def create(self, validated_data):
        validated_data.pop('audit_parameter', None)
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        # For PATCH requests, only update fields that are explicitly provided
        for field in ['equipment_type', 'line', 'plant', 'station']:
            # Only process the field if it's included in the request
            if field in validated_data:
                # If included but null/empty, skip it
                if validated_data[field] not in [None, 'null', '']:
                    setattr(instance, field, validated_data[field])
        
        # Update other fields that were provided
        for attr, value in validated_data.items():
            if attr not in ['equipment_type', 'line', 'plant', 'station', 'audit_parameter']:
                setattr(instance, attr, value)
        
        instance.save()
        return instance
    

class ScheduleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = equipment_models.ScheduleType
        fields = "__all__"
class ScheduleSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = equipment_models.Schedule
        fields = "__all__"  # Adjust this if needed
        extra_kwargs = {"assigned_by": {"read_only": True}}  # Read-only in input, but visible in response

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['plant'] = PlantSerializer(instance.plant).data
        line_serializer = LineSerializer(instance.line).data
        representation['line'] = {'id':line_serializer.get('id'),'name':line_serializer.get('name')}
        representation['equipment'] = EquipmentSerializer(instance.equipment).data
        station_serializer =StationSerializer(instance.station).data
        representation['station'] = {'id':station_serializer.get('id'),'name':station_serializer.get('name')}
        department_serializer =account_api_serializers.DepartmentSerializer(instance.department).data
        representation['department'] = {'id':department_serializer.get('id'),'name':department_serializer.get('name')}
        shedule_serializer =ScheduleTypeSerializer(instance.schedule_type).data
        representation['schedule_type'] = {'id':shedule_serializer.get('id'),'name':shedule_serializer.get('name')}
        representation['user'] = {"id":instance.user.id, 'name':instance.user.name}
        print("NOW:", timezone.now())
        print("SCHEDULE_DATE:", instance.schedule_date)

        representation['assigned_by'] = {"id":instance.assigned_by.id, 'name':instance.assigned_by.name}
        representation['status'] = "OVERDUE" if timezone.now() > instance.schedule_date else "PENDING"
        return representation
   

class MasterAuditParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = equipment_models.MasterAuditParameter
        fields = ['id', 'name']

class CheckPointSerializer(serializers.ModelSerializer):
    audit_parameter = serializers.ListField(required=False,write_only=True)

    class Meta:
        model = equipment_models.Checkpoint
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['audit_parameter'] = MasterAuditParameterSerializer(instance.audit_parameter).data
        equipment_data = EquipmentSerializer(instance.equipment).data
        representation['equipment'] = {
            "id": equipment_data.get("id"),
            "name": equipment_data.get("name"),
        }

        return representation


class CheckPointUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = equipment_models.Checkpoint
        fields = "__all__"
class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = equipment_models.Observation
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        current_user = self.context.get("current_user",None)
        request = self.context.get("request",None)

        if current_user is not None:
            representation['is_maintainer'] = True if current_user == instance.owner.manage_by else False
        
        if instance.action_auditor:
            representation['is_action_audior'] = True if current_user == instance.action_auditor else False
        else:
            representation['is_action_audior'] = False

        # Serialize the checkpoint and keep only 'id' and 'name'
        checkpoint_data = CheckPointSerializer(instance.checkpoint).data
        representation['checkpoint'] =  checkpoint_data.get("audit_parameter"),
        owner_data = account_api_serializers.UserSerializer(instance.owner).data
        representation['owner'] = {"id": owner_data.get("id"),"name": owner_data.get("name")}
        department_serializer =account_api_serializers.DepartmentSerializer(instance.department).data
        representation['department'] = {'id':department_serializer.get('id'),'name':department_serializer.get('name')}
        representation['plant'] = PlantSerializer(instance.plant).data
        representation['equipment'] = {
                                "equipment_id":instance.checkpoint.equipment.id,
                                "equipment_name":instance.checkpoint.equipment.name,
                                "equipment_type_id":instance.checkpoint.equipment.equipment_type.id,
                                "equipment_type":instance.checkpoint.equipment.equipment_type.name
                                }
        representation['schedule'] = {"id":instance.schedule.id,"fullfillment_date":instance.schedule.fullfillment_date,"status":instance.schedule.status} if instance.schedule else None
        if instance.action_owner:
            action_owner = account_api_serializers.UserSerializer(instance.action_owner).data
            representation['action_owner'] = {"id": action_owner.get("id"),"name": action_owner.get("name")}
        if instance.action_auditor:
            action_auditor = account_api_serializers.UserSerializer(instance.action_auditor).data
            representation['action_auditor'] = {"id": action_auditor.get("id"),"name": action_auditor.get("name")}

        audit = PerformAuditSerializer(instance.audit).data
        audit_image = audit.get("audit_image")
        if audit_image and request:
            audit_image = request.build_absolute_uri(audit_image)
        representation['audit'] = {"id":audit.get('id'),"remark":audit.get("remark"),"is_ok":audit.get("is_ok"),"audit_image":audit_image}
        return representation


class AuditSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = equipment_models.Audit
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Serialize the checkpoint and keep only 'id' and 'name'
        checkpoint_data = CheckPointSerializer(instance.checkpoint).data
        representation['checkpoint'] =  checkpoint_data.get("audit_parameter"),
        owner_data = account_api_serializers.UserSerializer(instance.auditor).data
        representation['owner'] = {"id": owner_data.get("id"),"name": owner_data.get("name")}
        department_serializer =account_api_serializers.DepartmentSerializer(instance.auditor.department).data
        representation['department'] = {'id':department_serializer.get('id'),'name':department_serializer.get('name')}
        representation['plant'] = PlantSerializer(instance.auditor.plant).data
        representation['equipment'] = {
                                "equipment_id":instance.checkpoint.equipment.id,
                                "equipment_name":instance.checkpoint.equipment.name,
                                "equipment_type_id":instance.checkpoint.equipment.equipment_type.id,
                                "equipment_type":instance.checkpoint.equipment.equipment_type.name
                                }
        representation['schedule'] = {"id":instance.schedule.id,"fullfillment_date":instance.schedule.fullfillment_date,"status":instance.schedule.status} if instance.schedule else None

        return representation

class EquipmentSerializer(serializers.ModelSerializer):
    audit_parameter = serializers.ListField(required=False)
    checkpoints = serializers.SerializerMethodField("get_checkpoints")

    class Meta:
        model = equipment_models.Equipment
        fields = "__all__"
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['plant'] = PlantSerializer(instance.plant).data
        line_serializer = LineSerializer(instance.line).data
        representation['line'] = {'id':line_serializer.get('id'),'name':line_serializer.get('name')}
        representation['equipment_type'] = EquipmentTypeSerializer(instance.equipment_type).data
        station_serializer =StationSerializer(instance.station).data
        representation['station'] = {'id':station_serializer.get('id'),'name':station_serializer.get('name')}

        return representation
    
    def get_checkpoints(self, instance):
        return instance.checkpoints.filter().values('audit_parameter__id','audit_parameter__name')
    
    def create(self, validated_data):
        # Remove 'audit_parameter' before creating the instance
        audit_parameter_data = validated_data.pop('audit_parameter', None)

        # Create Equipment instance
        equipment_instance = equipment_models.Equipment.objects.create(**validated_data)

        # Handle 'audit_parameter' if needed (e.g., save it elsewhere)
        if audit_parameter_data:
            # You may need to link or store this data in a related model
            pass  

        return equipment_instance
    

class PerformAuditSerializer(serializers.ModelSerializer):
    latitude = serializers.DecimalField(max_digits=10, decimal_places=6,write_only=True)
    longitude = serializers.DecimalField(max_digits=10, decimal_places=6,write_only=True)
    
    class Meta:
        model = equipment_models.Audit
        fields = ["id","is_ok","remark","checkpoint","latitude","longitude","request_status","approve_status","audit_image"]
        extra_kwargs = {"remark": {"read_only": True},"request_status": {"read_only": True},"approve_status": {"read_only": True}}  

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['checkpoint'] = CheckPointSerializer(instance.checkpoint).data
        return representation
 
class PerformAuditDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = equipment_models.Audit
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['checkpoint'] = CheckPointSerializer(instance.checkpoint).data
        return representation

class PerformBulkAuditSerializer(serializers.Serializer):
    audits = PerformAuditSerializer(many=True)  # Expecting an array of audit objects
    def validate_audits(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Expected a list of audit objects.")
        if not value:
            raise serializers.ValidationError("Audit list cannot be empty.")
        return value