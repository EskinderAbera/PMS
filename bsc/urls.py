from django.urls import path
from .views import *

urlpatterns = [
   path('<str:opt>/<str:pk>/', BSCAPIView.as_view()),
   path('add/kpi/<str:pk>/', AddActualKPIAPIView.as_view())
]