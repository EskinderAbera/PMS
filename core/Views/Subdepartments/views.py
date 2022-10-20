from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from core.models import *
from core.serializers import *

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