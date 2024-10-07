from rest_framework import serializers
from account import models as account_models
from django.contrib.auth.models import Group
from account import utils as account_utils
from equipment.api import serializers as equipment_api_serializers

class UserType(serializers.ModelSerializer):

    class Meta:
        model = account_models.UserType
        fields = ["id", "name"]

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = account_models.Department
        fields = ['id', 'name']


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = account_models.User
        fields = ['id', 'token_id','name','password','user_type','department','department','plant','groups','email']
    

    
    def create(self, validated_data):
        # Hash the password before creating the user
        validated_data['password'] = account_utils.PasswordManager.hash_password(validated_data.pop('password'))
        return super().create(validated_data)
    

class LoginSerializer(serializers.ModelSerializer):
    token_id = serializers.CharField()  # Define token_id manually without UniqueValidator

    class Meta:
        model = account_models.User
        fields = ['token_id','password']