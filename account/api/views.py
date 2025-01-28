from django.shortcuts import render
from rest_framework import views, generics
from account import query as account_query
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST)
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

class Department(UserPassesTestMixin,views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def test_func(self):
        return self.request.user.has_perm('account.can_view_department')

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
            return Response({"status": status, "data": serializer.data}, status=HTTP_200_OK)
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
    queryset = Group.objects.all()
    serializer_class = account_api_serializers.GroupSerializer

    @swagger_auto_schema(
        tags=['Group'],
        operation_summary="List all groups",
        operation_description="Retrieve a list of all groups."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    

class RegisterView(views.APIView):
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
            serializer.save()
            return Response({"status": status, 'data': serializer.data}, status=HTTP_200_OK)
        except Exception as e:
            return Response({"status": status, 'data': str(e)}, status=HTTP_400_BAD_REQUEST)


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
            return Response({"status": status, 'data': {'token':token}}, status=HTTP_200_OK)
        except Exception as e:
            return Response({"status": 400, 'data': str(e)}, status=HTTP_400_BAD_REQUEST)
