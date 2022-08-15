from unicodedata import name
from core.models import Role, Sub_SubDepartment, User, Department, SubDepartment
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.http import Http404

# Create your views here.

class BSCAPIView(APIView):

    def get(self, request, opt, pk, format=None):
        try:
            user = User.objects.get(id = pk)
        except User.DoesNotExist:
            return Response({'Error' : 'user does not exist!'}, status=status.HTTP_404_NOT_FOUND)

        if opt == 'kpi':
            kpis = user.bsc_user.all()
            KPIS = []
            for kpi in kpis:
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

                serialized_data['perspective_name'] = kpi.perspective.perspective_name
                serialized_data['objective_name'] = kpi.objective.objective_name
                serialized_data['numberOfmonthsLeft'] = numberOfmonthsLeft
                KPIS.append(serialized_data)
            return Response(KPIS, status=status.HTTP_200_OK) 
                
        elif opt == 'perspective':
            perspectives = user.bsc_perspective.all()
            serializer = PerspectiveSerializer(perspectives, many=True)

        elif opt == 'objective':
            objectives = user.bsc_objective.all()
            serializer = ObjectiveSerializer(objectives, many = True)

        else:
            return Response({'Error': 'Please check your url!'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, opt, pk, format=None):
        try:
            user = User.objects.get(id = pk)
        except User.DoesNotExist:
            return Response({'Error' : 'user does not exist!'}, status=status.HTTP_404_NOT_FOUND)

        if opt == 'kpi':
            serializer = CreateKPISerializer(data=request.data)
            if serializer.is_valid():
                if serializer.validated_data['kpi_unit_measurement'] == "Percentage":
                    serializer.validated_data['kpi_weight'] = float(serializer.validated_data['kpi_weight'])/100
                    serializer.validated_data['kpi_target'] = float(serializer.validated_data['kpi_target'])/100
                    serializer.save()  
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                elif serializer.validated_data['kpi_unit_measurement'] == "ETB" or serializer.validated_data['kpi_unit_measurement'] == "USD" or serializer.validated_data['kpi_unit_measurement'] =="Numbers":
                    serializer.validated_data['kpi_weight'] = float(serializer.validated_data['kpi_weight'])/100
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        elif opt == 'objective':
            serializer = ObjectiveSerializer(data=request.data)
            if serializer.is_valid():
                if serializer.validated_data['objective_weight'] == 0:
                    return Response({'Error': 'Objective weight can not be zero!'}, status=status.HTTP_406_NOT_ACCEPTABLE)
                serializer.validated_data['objective_weight'] = float(serializer.validated_data['objective_weight'])/100
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        elif opt == 'perspective':
            serializer = PerspectiveSerializer(data=request.data)
            if serializer.is_valid():
                if serializer.validated_data['perspective_weight'] == 0:
                    return Response({'Error': 'Perspective weight can not be zero!'}, status=status.HTTP_406_NOT_ACCEPTABLE)
                serializer.validated_data['perspective_weight'] = float(serializer.validated_data['perspective_weight'])/100
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'Error': 'Please check your url!'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, opt, pk):
        
        if opt == 'kpi':
            try:
                kpi = KPI.objects.get(kpi_id=pk)
            except KPI.DoesNotExist:
                return Response({'Error' : 'kpi does not exist!'}, status=status.HTTP_404_NOT_FOUND)
            serializer = CreateKPISerializer(kpi, data=request.data)

            if serializer.is_valid(raise_exception=True):
                if serializer.validated_data['kpi_unit_measurement'] == "Percentage":
                    serializer.validated_data['kpi_weight'] = float(serializer.validated_data['kpi_weight'])/100
                    serializer.validated_data['kpi_target'] = float(serializer.validated_data['kpi_target'])/100
                    serializer.save()  
                    return Response(serializer.data, status=status.HTTP_200_OK)
                elif serializer.validated_data['kpi_unit_measurement'] == "ETB" or serializer.validated_data['kpi_unit_measurement'] == "USD" or serializer.validated_data['kpi_unit_measurement'] =="Numbers":
                    serializer.validated_data['kpi_weight'] = float(serializer.validated_data['kpi_weight'])/100
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        elif opt == 'objective':
            try:
                objective = Objectives.objects.get(objective_id = pk)
            except Objectives.DoesNotExist:
                return Response({'Error' : 'objective does not exist!'}, status=status.HTTP_404_NOT_FOUND)
            serializer = ObjectiveSerializer(objective, data=request.data)

            if serializer.is_valid(raise_exception=True):
                if serializer.validated_data['objective_weight'] == 0:
                    return Response({'Error': 'Objective weight can not be zero!'}, status=status.HTTP_406_NOT_ACCEPTABLE)
                serializer.validated_data['objective_weight'] = float(serializer.validated_data['objective_weight'])/100
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        elif opt == 'perspective':
            try:
                perspective = Perspective.objects.get(perspective_id = pk)
            except Perspective.DoesNotExist:
                return Response({'Error' : 'perspective does not exist!'}, status=status.HTTP_404_NOT_FOUND)
            serializer = PerspectiveSerializer(perspective, data=request.data)

            if serializer.is_valid(raise_exception=True):
                if serializer.validated_data['perspective_weight'] == 0:
                    return Response({'Error': 'Perspective weight can not be zero!'}, status=status.HTTP_406_NOT_ACCEPTABLE)
                serializer.validated_data['perspective_weight'] = float(serializer.validated_data['perspective_weight'])/100
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class AddActualKPIAPIView(APIView):

    def get_object(self, pk):
        try:
            return KPI.objects.get(kpi_id=pk)
        except User.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        kpi = self.get_object(pk)
        if kpi.kpi_unit_measurement == "Percentage":
            if request.data.get("January"):
               request.data["January"] = float(request.data.get("January"))/100
            elif request.data.get("February"):
                request.data["February"] = float(request.data.get("February"))/100
            elif request.data.get("March"):
                request.data["March"] = float(request.data.get("March"))/100
            elif request.data.get("April"):
                request.data["April"] = float(request.data.get("April"))/100
            elif request.data.get("May"):
                request.data["May"] = float(request.data.get("May"))/100
            elif request.data.get("June"):
                request.data["June"] = float(request.data.get("June"))/100
            elif request.data.get("July"):
                request.data["July"] = float(request.data.get("July"))/100
            elif request.data.get("August"):
                request.data["August"] = float(request.data.get("August"))/100
            elif request.data.get("September"):
                request.data["September"] = float(request.data.get("September"))/100
            elif request.data.get("October"):
                request.data["October"] = float(request.data.get("October"))/100
            elif request.data.get("November"):
                request.data["November"] = float(request.data.get("November"))/100
            elif request.data.get("December"):
                request.data["December"] = float(request.data.get("December"))/100
        serializer = AddActualKPISerializer(kpi, data=request.data)
        if serializer.is_valid():
            if float(request.data.get("January", kpi.January)) != kpi.January and  float(request.data.get("January", kpi.January)) > float(0) and float(kpi.January) > float(0):
                return Response({"Error": "You have already added Actual Value for January!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("February", kpi.February)) != float(kpi.February) and  float(request.data.get("February")) > float(0) and float(kpi.February) > float(0):
                return Response({"Error": "You have already added Actual Value for February!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("March", kpi.March)) != float(kpi.March) and  float(request.data.get("March")) > float(0) and float(kpi.March) > float(0):
                return Response({"Error": "You have already added Actual Value for March!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("April", kpi.April)) != float(kpi.April) and  float(request.data.get("April")) > float(0) and float(kpi.April) > float(0):
                return Response({"Error": "You have already added Actual Value for April!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("May", kpi.May)) != float(kpi.May) and  float(request.data.get("May")) > float(0) and float(kpi.May) > float(0):
                return Response({"Error": "You have already added Actual Value for May!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("June", kpi.June)) != float(kpi.June) and  float(request.data.get("June")) > float(0) and float(kpi.June) > float(0):
                return Response({"Error": "You have already added Actual Value for June!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("July", kpi.July)) != float(kpi.July) and  float(request.data.get("July")) > float(0) and float(kpi.July) > float(0):
                return Response({"Error": "You have already added Actual Value for July!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("August", kpi.August)) != float(kpi.August) and  float(request.data.get("August")) > float(0) and float(kpi.August) > float(0):
                return Response({"Error": "You have already added Actual Value for August!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("September", kpi.September)) != float(kpi.September) and  float(request.data.get("September")) > float(0) and float(kpi.September) > float(0):
                return Response({"Error": "You have already added Actual Value for September!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("October", kpi.October)) != float(kpi.October) and  float(request.data.get("October")) > float(0) and float(kpi.October) > float(0):
                return Response({"Error": "You have already added Actual Value for October!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("November", kpi.November)) != float(kpi.November) and  float(request.data.get("November")) > float(0) and float(kpi.November) > float(0):
                return Response({"Error": "You have already added Actual Value for November!"}, status=status.HTTP_409_CONFLICT)
            elif float(request.data.get("December", kpi.December)) != float(kpi.December) and  float(request.data.get("December")) > float(0) and float(kpi.December) > float(0):
                return Response({"Error": "You have already added Actual Value for December!"}, status=status.HTTP_409_CONFLICT)
            else:
                if kpi.kpi_target == 0:
                    return Response({"Error":"KPI Target can't be zero!"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    serializer.save()
                    kpi.Score_January = ((kpi.January/kpi.kpi_target)*100) * kpi.kpi_weight
                    kpi.Score_February = ((kpi.February/kpi.kpi_target)*100) * kpi.kpi_weight
                    kpi.Score_March = ((kpi.March/kpi.kpi_target)*100) * kpi.kpi_weight
                    kpi.Score_April = ((kpi.April/kpi.kpi_target)*100) * kpi.kpi_weight
                    kpi.Score_May = ((kpi.May/kpi.kpi_target)*100) * kpi.kpi_weight
                    kpi.Score_June = ((kpi.June/kpi.kpi_target)*100) * kpi.kpi_weight
                    kpi.Score_July = ((kpi.July/kpi.kpi_target)*100) * kpi.kpi_weight
                    kpi.Score_August = ((kpi.August/kpi.kpi_target)*100) * kpi.kpi_weight
                    kpi.Score_September = ((kpi.September/kpi.kpi_target)*100) * kpi.kpi_weight
                    kpi.Score_October = ((kpi.October/kpi.kpi_target)*100) * kpi.kpi_weight
                    kpi.Score_November = ((kpi.November/kpi.kpi_target)*100) * kpi.kpi_weight
                    kpi.Score_December = ((kpi.December/kpi.kpi_target)*100) * kpi.kpi_weight
                    kpi.aggregate = kpi.Score_January + kpi.Score_February + kpi.Score_March + kpi.Score_April + kpi.Score_May + kpi.Score_June + kpi.Score_July + kpi.Score_August + kpi.Score_September +  kpi.Score_October + kpi.Score_November + kpi.Score_December
                    kpi.save()
                    serializer = KPISerializer(kpi)
                    return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    

