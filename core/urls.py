from django.urls import path
from .views import *

urlpatterns = [
    path('department/', department_list),    
    path('department/<str:pk>/', department_detail),  
    path('role/', role_list),
    path('role_detail/<str:pk>/', role_detail),
]