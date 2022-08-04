from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework import status
from .models import *
from .serializers import *

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