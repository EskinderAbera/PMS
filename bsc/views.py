from core.models import Role, User, Department, SubDepartment
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.parsers import JSONParser

# Create your views here.

class GetCEOKPIAPIView(APIView):

    def get(self, request, dept, format=None):
        department = Department.objects.get(dept_name = dept)
        user = User.objects.get(department = department)
        kpis = KPI.objects.all().filter(user = user)
        KPIS = []
        for kpi in kpis:
            actual_aggregate = kpi.January + kpi.February + kpi.March + kpi.April + kpi.May + kpi.June + kpi.July + kpi.August + kpi.September +  kpi.October + kpi.November + kpi.December
            serializer = KPISerializer(kpi)
            serialized_data = serializer.data
            numberOfmonthsLeft = 0
            if(kpi.January<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.February<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.March<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.April<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.May<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.June<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.July<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.August<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.September<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.October<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.November<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.December<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            serialized_data['actual_aggregate'] = actual_aggregate
            serialized_data['numberOfmonthsLeft'] = numberOfmonthsLeft
            perspectives = Perspective.objects.filter(perspective_name = serialized_data['perspective'])
            objectives = Objectives.objects.filter(objective_name = serialized_data['objective'])
            for perspective in perspectives:
                serialized_data['perspective_weight'] = perspective.perspective_weight
            for objective in objectives:
                serialized_data['objective_weight'] = objective.objective_weight
            KPIS.append(serialized_data)
        return Response(sorted(KPIS, key=lambda x: x['perspective']), status=status.HTTP_200_OK)


class GetVPKPIAPIView(APIView):
    def get(self, request, dept, format=None):
        department = Department.objects.get(dept_name = dept)
        user = User.objects.all().get(department = department, subdepartment = None)
        kpis = KPI.objects.all().filter(user = user)
        KPIS = []
        for kpi in kpis:
            actual_aggregate = kpi.January + kpi.February + kpi.March + kpi.April + kpi.May + kpi.June + kpi.July + kpi.August + kpi.September +  kpi.October + kpi.November + kpi.December
            serializer = KPISerializer(kpi)
            serialized_data = serializer.data
            numberOfmonthsLeft = 0
            if(kpi.January<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.February<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.March<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.April<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.May<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.June<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.July<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.August<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.September<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.October<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.November<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.December<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            serialized_data['actual_aggregate'] = actual_aggregate
            serialized_data['numberOfmonthsLeft'] = numberOfmonthsLeft
            serialized_data['perspective_weight'] = kpi.perspective.perspective_weight
            serialized_data['objective_weight'] = kpi.objective.objective_weight
            KPIS.append(serialized_data)
        return Response(sorted(KPIS, key=lambda x: x['perspective']), status=status.HTTP_200_OK)

class GetDirectorKPIAPIView(APIView):
    def get(self, request, dept, subdept, format=None):
        department = Department.objects.get(dept_name = dept)
        subdepartment = SubDepartment.objects.get(department = department, name = subdept)
        user = User.objects.all().get(department = department, subdepartment = subdepartment.id)
        kpis = KPI.objects.all().filter(user = user)
        print(len(kpis))
        KPIS = []
        for kpi in kpis:
            actual_aggregate = kpi.January + kpi.February + kpi.March + kpi.April + kpi.May + kpi.June + kpi.July + kpi.August + kpi.September +  kpi.October + kpi.November + kpi.December
            serializer = KPISerializer(kpi)
            serialized_data = serializer.data
            numberOfmonthsLeft = 0
            if(kpi.January<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.February<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.March<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.April<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.May<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.June<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.July<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.August<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.September<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.October<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.November<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            if(kpi.December<=0):
                numberOfmonthsLeft=numberOfmonthsLeft + 1
            serialized_data['actual_aggregate'] = actual_aggregate
            serialized_data['numberOfmonthsLeft'] = numberOfmonthsLeft
            serialized_data['perspective_weight'] = kpi.perspective.perspective_weight
            serialized_data['objective_weight'] = kpi.objective.objective_weight
            KPIS.append(serialized_data)
        return Response(sorted(KPIS, key=lambda x: x['perspective']), status=status.HTTP_200_OK)

class CeoPerspectiveAPIView(APIView):
    def get(self, request, dept, format=None):
        department = Department.objects.get(dept_name = dept)
        user = User.objects.get(department = department)
        perspectives = user.bsc_perspective.all()
        newPerspectives = []
        for perspective in perspectives:
            serializer = PerspectiveSerializer(perspective)
            serialized_data = serializer.data
            serialized_data['user'] = perspective.user.username
            newPerspectives.append(serialized_data)
        return Response(newPerspectives, status=status.HTTP_200_OK)


    def post(self, request, dept, format=None):
        data = JSONParser().parse(request)
        serializer = PerspectiveSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class CeoObjectiveAPIView(APIView):
    def get(self, request, dept, format=None):
        department = Department.objects.get(dept_name = dept)
        user = User.objects.get(department = department)
        objectives = user.bsc_objective.all()
        newObjectives = []
        for objective in objectives:
            serializer = ObjectiveSerializer(objective)
            serialized_data = serializer.data
            serialized_data['user'] = objective.user.username
            newObjectives.append(serialized_data)
        return Response(newObjectives, status=status.HTTP_200_OK)


    def post(self, request, dept, format=None):
        data = JSONParser().parse(request)
        serializer = ObjectiveSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class VPPerspectiveAPIView(APIView):
    def get(self, request, dept, role, format=None):
        department = Department.objects.get(dept_name = dept)
        role = Role.objects.get(role_name = role)
        user = User.objects.get(department = department, role = role)
        perspectives = user.bsc_perspective.all()
        newPerspectives = []
        for perspective in perspectives:
            serializer = PerspectiveSerializer(perspective)
            serialized_data = serializer.data
            serialized_data['user'] = perspective.user.username
            newPerspectives.append(serialized_data)
        return Response(newPerspectives, status=status.HTTP_200_OK)


    def post(self, request, dept, role, format=None):
        data = JSONParser().parse(request)
        serializer = PerspectiveSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class VPObjectiveAPIView(APIView):
    def get(self, request, dept, role, format=None):
        department = Department.objects.get(dept_name = dept)
        role = Role.objects.get(role_name = role)
        user = User.objects.get(department = department, role=role)
        objectives = user.bsc_objective.all()
        newObjectives = []
        for objective in objectives:
            serializer = ObjectiveSerializer(objective)
            serialized_data = serializer.data
            serialized_data['user'] = objective.user.username
            serialized_data['perspective'] = objective.perspective.perspective_name
            newObjectives.append(serialized_data)
        return Response(newObjectives, status=status.HTTP_200_OK)


    def post(self, request, dept, role, format=None):
        data = JSONParser().parse(request)
        serializer = ObjectiveSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class DirectorPerspectiveAPIView(APIView):
    def get(self, request, dept, subdept, role, format=None):
        department = Department.objects.get(dept_name = dept)
        subdepartment = SubDepartment.objects.get(name = subdept)
        role = Role.objects.get(role_name = role)
        user = User.objects.get(department = department, role = role, subdepartment = subdepartment)
        perspectives = user.bsc_perspective.all()
        newPerspectives = []
        for perspective in perspectives:
            serializer = PerspectiveSerializer(perspective)
            serialized_data = serializer.data
            serialized_data['user'] = perspective.user.username
            newPerspectives.append(serialized_data)
        return Response(newPerspectives, status=status.HTTP_200_OK)


    def post(self, request, dept, subdept, role, format=None):
        data = JSONParser().parse(request)
        serializer = PerspectiveSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class DirectorObjectiveAPIView(APIView):
    def get(self, request, dept, role, subdept, format=None):
        department = Department.objects.get(dept_name = dept)
        subdepartment = SubDepartment.objects.get(name = subdept)
        role = Role.objects.get(role_name = role)
        user = User.objects.get(department = department, role=role, subdepartment = subdepartment)
        objectives = user.bsc_objective.all()
        newObjectives = []
        for objective in objectives:
            serializer = ObjectiveSerializer(objective)
            serialized_data = serializer.data
            serialized_data['user'] = objective.user.username
            serialized_data['perspective'] = objective.perspective.perspective_name
            newObjectives.append(serialized_data)
        return Response(newObjectives, status=status.HTTP_200_OK)


    def post(self, request, dept, role, subdept, format=None):
        data = JSONParser().parse(request)
        serializer = ObjectiveSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

