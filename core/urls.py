from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')

urlpatterns = [
    *routes.urls,
    path('department/', department_list),    
    path('department/<str:pk>/', department_detail),  
    path('role/', role_list),
    path('role_detail/<str:pk>/', role_detail),
]