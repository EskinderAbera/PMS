from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import MultiPartParser, FormParser

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
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SubDepartmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status = 400)

@api_view(['GET', 'POST'])
def sub_subdepartment_list(request):

    if request.method == 'GET':
        subdepartments = Sub_SubDepartment.objects.all()
        serializer = SubSubDepartmentSerializer(subdepartments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SubSubDepartmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status = 400)


@api_view(['GET', 'PUT', 'DELETE'])
def sub_subdepartment_detail(request, pk):
    try:
        subsubdepartment = Sub_SubDepartment.objects.get(pk=pk)
    except Sub_SubDepartment.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = SubSubDepartmentSerializer(subsubdepartment)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SubSubDepartmentSerializer(subsubdepartment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        subsubdepartment.delete()
        return HttpResponse(status=204)


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
            serialized_data['actual_aggregate'] = actual_aggregate
            serialized_data['perspective_weight'] = kpi.perspective.perspective_weight
            serialized_data['objective_weight'] = kpi.objective.objective_weight
            KPIS.append(serialized_data)
        return Response(sorted(KPIS, key=lambda x: x['perspective']), status=status.HTTP_200_OK) 


class LoginView(ModelViewSet, TokenObtainPairView):
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
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RegistrationViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        serialized_data = serializer.data
        
        return Response(
            {
                "user": serialized_data,
                "refresh": res["refresh"],
                "token": res["access"],
            },
            status=status.HTTP_201_CREATED,
        )

# class UserList(APIView):

#     def get(self, request, format=None):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class UserEdit(APIView):
    def put(self, request, pk):
        try:
            user = User.objects.get(id = pk)
        except User.DoesNotExist:
            return Response({'Error' : 'User does not exist!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IndividualAPI(APIView):
    def get(self, request):
        individuals = Individuals.objects.all()
        serializer = IndividualSerializer(individuals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = IndividualSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class EditIndividual(APIView):
    def put(self, request, pk):
        try:
            individual = Individuals.objects.get(id=pk)
        except Individuals.DoesNotExist:
            return Response({'Error' : 'Individual does not exist!'}, status=status.HTTP_404_NOT_FOUND)

        serializer = IndividualSerializer(individual, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@parser_classes((MultiPartParser, FormParser, JSONParser))
class ProfilePicture(APIView):

    def get(self, request):
        pics = ProfilePic.objects.all()
        serializer = ProfileSerializer(pics, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            user = User.objects.get(id = request.data['user'])
        except User.DoesNotExist:
            return Response({'Error' : 'User does not exist!'}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = ProfileSerializer(data = request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
                

@parser_classes((MultiPartParser, FormParser, JSONParser))
class EditProfilePic(APIView):

    def put(self, request, pk):
        try:
            profile = ProfilePic.objects.get(id = pk)
        except ProfilePic.DoesNotExist:
            return Response({'Error' : 'Profile does not exist!'}, status=status.HTTP_404_NOT_FOUND)

        else:
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            

