from django.shortcuts import render
from rest_framework import views, generics
from account import query as account_query
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,HTTP_201_CREATED,HTTP_403_FORBIDDEN,HTTP_404_NOT_FOUND)
from shared import serializers as shared_serializers
from account.api import serializers as account_api_serializers
from account import models as account_models
from django.contrib.auth.models import Group
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from django.contrib.auth.mixins import UserPassesTestMixin
from account import permissions as account_permissions
from account import utils as account_utils
# Create your views here.

class Department(views.APIView):
    permission_classes = [permissions.IsAuthenticated,account_permissions.IsPortalAdmin|account_permissions.IsSuperAdmin]


    @swagger_auto_schema(
        tags=['Department'],
        operation_summary="List all departments",
        operation_description="Retrieve a list of all departments."
    )
    def get(self, request, *args, **kwargs):
        status,data = None, None
        try:
            departments = account_query.DepartmentRepository().get_all_departments()
            status,data = shared_serializers.SerializerValidator(account_api_serializers.DepartmentSerializer).serialize_queryset(queryset=departments)
            return Response({"status": status, "data":data}, HTTP_200_OK)
        except Exception as e:
            return Response({"status": status, "data": str(e)}, HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=['Department'],
        request_body=account_api_serializers.DepartmentSerializer,
        operation_summary="Create a new department",
        operation_description="Create a new department using the provided details."
    )
    def post(self, request, *args, **kwargs):
        try:
            status,serializer = shared_serializers.SerializerValidator(account_api_serializers.DepartmentSerializer).validate(payload=request.data)
            if status in [400]:
                return Response({"status": status, "data": serializer.errors}, status=HTTP_400_BAD_REQUEST)
            account_query.DepartmentRepository().add_department(serializer.data['name'])
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            return Response({"status": status, "data": str(e)}, HTTP_400_BAD_REQUEST)


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = account_models.Department.objects.all()
    serializer_class = account_api_serializers.DepartmentSerializer
    lookup_field = 'pk'

    @swagger_auto_schema(
        tags=['Department'],
        operation_summary="Retrieve a department",
        operation_description="Get the details of a department by its ID."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Department'],
        request_body=account_api_serializers.DepartmentSerializer,
        operation_summary="Update a department",
        operation_description="Update the details of a department by its ID."
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Department'],
        operation_summary="Delete a department",
        operation_description="Delete a department by its ID."
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def put(self, request, *args, **kwargs):
        pass
 
class GroupView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Group.objects.all()
    serializer_class = account_api_serializers.GroupSerializer
    
    @swagger_auto_schema(
        tags=['Group'],
        operation_summary="List all groups",
        operation_description="Retrieve a list of all groups."
    )
    def get(self, request, *args, **kwargs):
        '''
        if user is Portal Admin:
            return Super Admin,Admin,Auditor
        elif user is Super Admin:
            return Admin,Auditor
        elif user is Admin:
            return Auditor
        '''
        user_type = account_query.GroupQuery().get_user_type_level(request.user)        
        return Response({"status": "200", "data": user_type}, status=HTTP_200_OK)

    

class RegisterView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        tags=['User'],
        request_body=account_api_serializers.UserSerializer,
        operation_summary="Register a new user",
        operation_description="Create a new user account with the provided details."
    )
    def post(self, request, *args, **kwargs):
        try:
            status,serializer = shared_serializers.SerializerValidator(serializer_class=account_api_serializers.UserSerializer).validate(payload=request.data)
            if status in [400]:
                return Response({"status": status, 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)
            serializer.save(manage_by = self.request.user,department=request.user.department,plant=request.user.plant)
            return Response({"status": status, 'data': "Registration Successfull"}, status=HTTP_201_CREATED)
        except Exception as e:
            return Response({"status": status, 'data': str(e)}, status=HTTP_400_BAD_REQUEST)



class ListUserView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = account_models.User.objects.all()
    serializer_class = account_api_serializers.UserSerializer
    @swagger_auto_schema(
        tags=['User'],
        operation_summary="List all users",
        operation_description="Retrieve a list of users"
    )
    def get(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(manage_by = request.user)
        return super().get(request, *args, **kwargs)

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,account_permissions.IsAdmin|account_permissions.IsPortalAdmin|account_permissions.IsSuperAdmin]

    queryset = account_models.User.objects.all()
    serializer_class = account_api_serializers.UserSerializer
    @swagger_auto_schema(
        tags=['User'],
        operation_summary="Retrieve a user",
        operation_description="Get a user by its ID."
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['User'],
        operation_summary="Update a user",
        operation_description="Update an existing user by its ID."
    )
    def patch(self, request, *args, **kwargs):
    #     user_obj = account_query.UserQuery().get_user_by_id(kwargs.get('pk'))
    #     if user_obj is None:
    #         return Response({"status": 404, "data": "User not found"}, status=HTTP_404_NOT_FOUND)
    #     if request.user !=user_obj.manage_by:
    #         return Response({"status": 403, "data": "Unauthorized to update this user"}, status=HTTP_403_FORBIDDEN)
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['User'],
        operation_summary="Delete a user",
        operation_description="Delete a user by its ID."
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def put(self, request, *args, **kwargs):
        pass

class LoginView(views.APIView):
    @swagger_auto_schema(
        tags=['User'],
        request_body=account_api_serializers.LoginSerializer,
        operation_summary="Login a user",
        operation_description="Login a  user account with the provided details."
    )
    def post(self,request,*args,**kwargs):
        try:
            status,serializer = shared_serializers.SerializerValidator(serializer_class=account_api_serializers.LoginSerializer).validate(payload=request.data)
            if status in [400]:
                return Response({"status": status, 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)
            user = account_query.UserQuery().get_user_by_token_id(token_id=serializer.data['token_id'])
            if user is None or not user.check_password(serializer.data['password']):
                return Response({"status":400,"data":"Invalid credentials"},status=HTTP_400_BAD_REQUEST)
            
            token = account_query.TokenQuery().generate_token(user = user)
            user_type = account_query.GroupQuery().get_user_type_level(user)
            role = account_query.GroupQuery().get_user_role(user)        
            return Response({"status": status, 'data': {'token':token,"role":role,"user_type":user_type}}, status=HTTP_200_OK)
        except Exception as e:
            return Response({"status": 400, 'data': str(e)}, status=HTTP_400_BAD_REQUEST)




class CurrentUserDetails(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = account_models.User.objects.all()
    serializer_class = account_api_serializers.UserSerializer

    @swagger_auto_schema(
        tags=['User'],
        operation_summary="Retrieve current user details",
        operation_description="Get the details of the current authenticated user."
    )
    def get(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(id=request.user.id)
        return super().get(request, *args, **kwargs)  # Use super() to prevent recursion
