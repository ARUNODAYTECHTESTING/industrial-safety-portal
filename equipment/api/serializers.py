from rest_framework import serializers
from equipment import models as equipment_models
from account.api import serializers as account_api_serializers
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

class EquipmentSerializer(serializers.ModelSerializer):
    audit_parameter = serializers.ListField(required=False)
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
class ScheduleSerializer(serializers.ModelSerializer):
    plant = serializers.SerializerMethodField()
    department= serializers.SerializerMethodField()
    line = serializers.SerializerMethodField()
    station = serializers.SerializerMethodField()
    equipment_type = serializers.SerializerMethodField()

    class Meta:
        model = equipment_models.Schedule
        fields = "__all__"  # Adjust this if needed

class MasterAuditParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = equipment_models.MasterAuditParameter
        fields = ['id', 'name']

class CheckPointSerializer(serializers.ModelSerializer):
    audit_parameter = serializers.ListField(required=False,write_only=True)

    class Meta:
        model = equipment_models.Checkpoint
        fields = "__all__"



class ObservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = equipment_models.Observation
        fields = "__all__"
