from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/new/login', LoginView, basename='new-login')
routes.register(r'auth/register', RegistrationViewSet,
                basename='auth-register')

urlpatterns = [
    *routes.urls,
    path('department/', department_list),    
    path('department/<str:pk>/', department_detail),        
    path('role/', role_list),
    path('role_detail/<str:pk>/', role_detail),
    path('subdepartment/', subdepartment_list),
    path('subdepartment_detail/<str:pk>/', subdepartment_detail),
    path('users/', UserList.as_view()),
    path('user/<str:pk>/', UserEdit.as_view()),
    path('subsub/', sub_subdepartment_list),
    path('subsub/<str:pk>/', sub_subdepartment_detail),
    path('individual/', IndividualAPI.as_view()),
    path('individual/<str:pk>/', EditIndividual.as_view()),
    path('profilepic/', ProfilePicture.as_view()),
    path('editprofile/<str:pk>/', EditProfilePic.as_view())
]