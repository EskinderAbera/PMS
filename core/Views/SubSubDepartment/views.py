from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from core.models import *
from core.serializers import *


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
