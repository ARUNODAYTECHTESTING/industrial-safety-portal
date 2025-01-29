from django.urls import path
from account.api import views as account_api_views
urlpatterns = [
    path('department/',account_api_views.Department.as_view(),name = 'department'),
    path('department-details/<int:pk>/',account_api_views.DepartmentDetailView.as_view(),name = 'department-view'),
    path('groups/',account_api_views.GroupView.as_view(),name='groups'),
    path('register/',account_api_views.RegisterView.as_view(),name='register'),
    path('login/',account_api_views.LoginView.as_view(),name='login'),
]