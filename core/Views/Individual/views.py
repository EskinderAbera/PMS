from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from core.models import *
from core.serializers import *


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