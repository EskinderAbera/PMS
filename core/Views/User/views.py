from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from core.models import *
from core.serializers import *
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import MultiPartParser, FormParser


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
            if serialized_data['kpi_unit_measurement'] == 'Percentage' :
                serialized_data['kpi_q1'] = int(serialized_data['kpi_q1'])/100
                serialized_data['kpi_q2'] = int(serialized_data['kpi_q2'])/100
                serialized_data['kpi_q3'] = int(serialized_data['kpi_q3'])/100
                serialized_data['kpi_q4'] = int(serialized_data['kpi_q4'])/100
                KPIS.append(serialized_data)
            else:
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

# class UserList( mixins.RetrieveModelMixin,
#                 mixins.UpdateModelMixin,
#                 mixins.DestroyModelMixin,
#                 generics.GenericAPIView ):

#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

class UserList(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
