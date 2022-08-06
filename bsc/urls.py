from django.urls import path
from .views import *

urlpatterns = [
   path('ceo/kpi/<str:dept>/', GetCEOKPIAPIView.as_view()),
   path('ceo/perspective/<str:dept>/', CeoPerspectiveAPIView.as_view()),
   path('ceo/objective/<str:dept>/', CeoObjectiveAPIView.as_view()),
   path('vp/kpi/<str:dept>/', GetVPKPIAPIView.as_view()),
   path('vp/perspective/<str:dept>/<str:role>/', VPPerspectiveAPIView.as_view()),
   path('vp/objective/<str:dept>/<str:role>/', VPObjectiveAPIView.as_view()),
   path('dir/kpi/<str:dept>/<str:subdept>/', GetDirectorKPIAPIView.as_view()),
   path('dir/perspective/<str:dept>/<str:subdept>/<str:role>/', DirectorPerspectiveAPIView.as_view()),
   path('dir/objective/<str:dept>/<str:subdept>/<str:role>/', DirectorObjectiveAPIView.as_view()),
]