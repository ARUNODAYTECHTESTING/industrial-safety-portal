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
    plant = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()

    class Meta:
        model = equipment_models.Line
        fields = ['id', 'name','plant','department']

    def get_plant(self, obj):
        palant =  PlantSerializer(obj.plant).data if obj.plant else None
        if palant is not None:
            return {
                'id': palant['id'],
                'name': palant['name'],
            }
    def get_department(self, obj):
        department =  account_api_serializers.DepartmentSerializer(obj.department).data if obj.department else None
        if department is not None:
            return {
                'id': department['id'],
                'name': department['name'],
            }

class StationSerializer(serializers.ModelSerializer):
    plant = serializers.SerializerMethodField()
    department= serializers.SerializerMethodField()
    line = serializers.SerializerMethodField()

    class Meta:
        model = equipment_models.Station
        fields = ['id', 'name','plant','department','line']
        
    def get_plant(self, obj):
        palant =  PlantSerializer(obj.plant).data if obj.plant else None
        if palant is not None:
            return {
                'id': palant['id'],
                'name': palant['name'],
            }
    def get_department(self, obj):
        department =  account_api_serializers.DepartmentSerializer(obj.department).data if obj.department else None
        if department is not None:
            return {
                'id': department['id'],
                'name': department['name'],
            }
        
    def get_line(self, obj):
        line =  LineSerializer(obj.line).data if obj.line else None
        if line is not None:
            return {
                'id': line['id'],
                'name': line['name'],
            }

class EquipmentSerializer(serializers.ModelSerializer):
    plant = serializers.SerializerMethodField()
    department= serializers.SerializerMethodField()
    line = serializers.SerializerMethodField()
    equipment_type = serializers.SerializerMethodField()

    class Meta:
        model = equipment_models.Equipment
        fields = ['id', 'name', 'plant', 'department', 'line', 'equipment_type', 'qr']

    def get_plant(self, obj):
        palant =  PlantSerializer(obj.plant).data if obj.plant else None
        if palant is not None:
            return {
                'id': palant['id'],
                'name': palant['name'],
            }
    def get_department(self, obj):
        department =  account_api_serializers.DepartmentSerializer(obj.department).data if obj.department else None
        if department is not None:
            return {
                'id': department['id'],
                'name': department['name'],
            }
        
    def get_line(self, obj):
        line =  LineSerializer(obj.line).data if obj.line else None
        if line is not None:
            return {
                'id': line['id'],
                'name': line['name'],
            }
    def get_equipment_type(self, obj):
        eq_type =  EquipmentTypeSerializer(obj.equipment_type).data if obj.equipment_type else None
        if eq_type is not None:
            return {
                'id': eq_type['id'],
                'name': eq_type['name'],
            }
        
class CheckListSerializer(serializers.ModelSerializer):
    plant = serializers.SerializerMethodField()
    department= serializers.SerializerMethodField()
    line = serializers.SerializerMethodField()
    station = serializers.SerializerMethodField()
    equipment = serializers.SerializerMethodField()

    class Meta:
        model = equipment_models.CheckList
        fields = ['id', 'name', 'plant', 'department', 'line', 'station', 'equipment', 'image']

    def get_plant(self, obj):
        palant =  PlantSerializer(obj.plant).data if obj.plant else None
        if palant is not None:
            return {
                'id': palant['id'],
                'name': palant['name'],
            }
    def get_department(self, obj):
        department =  account_api_serializers.DepartmentSerializer(obj.department).data if obj.department else None
        if department is not None:
            return {
                'id': department['id'],
                'name': department['name'],
            }
    def get_line(self, obj):
        line =  LineSerializer(obj.line).data if obj.line else None
        if line is not None:
            return {
                'id': line['id'],
                'name': line['name'],
            }
    def get_station(self, obj):
        station =  StationSerializer(obj.station).data if obj.station else None
        if station is not None:
            return {
                'id': station['id'],
                'name': station['name'],
            }
        
    def get_equipment(self, obj):
        equipment =  EquipmentSerializer(obj.equipment).data if obj.equipment else None
        if equipment is not None:
            return {
                'id': equipment['id'],
                'name': equipment['name'],
            }
        
class ScheduleSerializer(serializers.ModelSerializer):
    plant = serializers.SerializerMethodField()
    department= serializers.SerializerMethodField()
    line = serializers.SerializerMethodField()
    station = serializers.SerializerMethodField()
    equipment_type = serializers.SerializerMethodField()

    class Meta:
        model = equipment_models.Schedule
        fields = "__all__"  # Adjust this if needed

    def get_plant(self, obj):
        palant =  PlantSerializer(obj.plant).data if obj.plant else None
        if palant is not None:
            return {
                'id': palant['id'],
                'name': palant['name'],
            }
    def get_department(self, obj):
        department =  account_api_serializers.DepartmentSerializer(obj.department).data if obj.department else None
        if department is not None:
            return {
                'id': department['id'],
                'name': department['name'],
            }
        
    def get_line(self, obj):
        line =  LineSerializer(obj.line).data if obj.line else None
        if line is not None:
            return {
                'id': line['id'],
                'name': line['name'],
            }
    def get_station(self, obj):
        station =  StationSerializer(obj.station).data if obj.station else None
        if station is not None:
            return {
                'id': station['id'],
                'name': station['name'],
            }
    def get_equipment_type(self, obj):
        eq_type =  EquipmentTypeSerializer(obj.equipment_type).data if obj.equipment_type else None
        if eq_type is not None:
            return {
                'id': eq_type['id'],
                'name': eq_type['name'],
            }
        