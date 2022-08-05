from django.urls import path
from .views import *

urlpatterns = [
   path('ceo/kpi/<str:dept>/', GetCEOKPIAPIView.as_view()),
   path('vp/kpi/<str:dept>/', GetVPKPIAPIView.as_view()),
   path('dir/kpi/<str:dept>/<str:subdept>/', GetDirectorKPIAPIView.as_view()),
]