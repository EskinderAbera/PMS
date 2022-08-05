from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

@api_view(['GET', 'POST'])
def department_list(request):

    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status = 400)


@api_view(['GET', 'PUT', 'DELETE'])
def department_detail(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = DepartmentSerializer(department)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DepartmentSerializer(department, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        department.delete()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
def subdepartment_list(request):

    if request.method == 'GET':
        subdepartments = SubDepartment.objects.all()
        serializer = SubDepartmentSerializer(subdepartments, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SubDepartmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status = 400)


@api_view(['GET', 'PUT', 'DELETE'])
def subdepartment_detail(request, pk):
    try:
        subdepartment = SubDepartment.objects.get(pk=pk)
    except Department.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = SubDepartmentSerializer(subdepartment)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SubDepartmentSerializer(subdepartment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        subdepartment.delete()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
def role_list(request):
    
    if request.method == 'GET':
        snippets = Role.objects.all()
        serializer = RoleSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RoleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def role_detail(request, pk):
    try:
        role = Role.objects.get(pk=pk)
    except Role.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RoleSerializer(role)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RoleSerializer(role, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        role.delete()
        return HttpResponse(status=204)

class LoginViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = LoginSerializers
    permission_classes = (AllowAny,)
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        serialized_data = serializer.validated_data
        user = User.objects.get(id = serialized_data['user']['id'])
        kpis = user.bsc_user.all()
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
            serialized_data['perspective_weight'] = kpi.perspective.perspective_weight
            serialized_data['objective_weight'] = kpi.objective.objective_weight
            serialized_data['numberOfmonthsLeft'] = numberOfmonthsLeft
            KPIS.append(serialized_data)
        return Response(sorted(KPIS, key=lambda x: x['perspective']), status=status.HTTP_200_OK) 


# class RegistrationViewSet(ModelViewSet, TokenObtainPairView):
#     serializer_class = RegisterSerializer
#     permission_classes = (AllowAny,)
#     http_method_names = ["post"]

#     def create(self, request, *args, **kwargs):
#         role = Role.objects.get(role_name = request.data.get("role"))
#         department = Department.objects.get(dept_name = request.data.get("department"))
#         subdepartment = SubDepartment.objects.get(name = request.data.get("subdepartment"))
#         request.data['department'] = department.dept_id
#         request.data['role'] = role.role_id
#         request.data['subdepartment'] = subdepartment.id
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         refresh = RefreshToken.for_user(user)
#         res = {
#             "refresh": str(refresh),
#             "access": str(refresh.access_token),
#         }
#         serialized_data = serializer.data
#         serialized_data['role'] = role.role_name
#         serialized_data['department'] = department.dept_name
#         serialized_data['subdepartment'] = subdepartment.name

#         return Response(
#             {
#                 "user": serialized_data,
#                 "refresh": res["refresh"],
#                 "token": res["access"],
#             },
#             status=status.HTTP_201_CREATED,
#         )

class UserList(APIView):

    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def put(self, request, pk, format=None):
    #     user = self.get_object(pk)
    #     serializer = RegisterSerializer(user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     user = self.get_object(pk)
    #     user.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
