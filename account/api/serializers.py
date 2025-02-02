from rest_framework import serializers
from account import models as account_models
from django.contrib.auth.models import Group
from account import utils as account_utils
from equipment.api import serializers as equipment_api_serializers
from equipment.api.serializers import PlantSerializer
from account import query as account_query
class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = account_models.Department
        fields = ['id', 'name']


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(source = 'groups')
    class Meta:
        model = account_models.User
        fields = ['id','name','password','user_type','department','plant','email','phone']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['plant'] = instance.plant.name if instance.plant else None
        representation["user_type"] = instance.groups.filter().first().name if instance.groups.filter().first() else None
        representation["department"] = instance.department.name if instance.department else None

        return representation
    
    def create(self, validated_data):
        # Hash the password before creating the user
        validated_data['password'] = account_utils.PasswordManager.hash_password(validated_data.pop('password'))
        return super().create(validated_data)
    

class LoginSerializer(serializers.ModelSerializer):
    token_id = serializers.CharField()  # Define token_id manually without UniqueValidator

    class Meta:
        model = account_models.User
        fields = ['token_id','password']



