from rest_framework import serializers
from .models import *
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['dept_id', 'dept_name']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['role_id', 'role_name', 'hierarchy']

class SubDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDepartment
        fields = ['id', 'name', 'department']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "role",
            "department",
            "subdepartment",
            "is_active"
        ]
        read_only_field = ["is_active"]


class LoginSerializers(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["user"] = UserSerializer(self.user).data
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class RegisterSerializer(UserSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=True
    )
    username = serializers.CharField(required=True, max_length=128)
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "password",
            "username",
            "department",
            "role",
            "subdepartment",
            "is_active",

        ]

    def create(self, validated_data):
            try:
                user = User.objects.get(
                    username=validated_data["username"])
            except ObjectDoesNotExist:
                user = User.objects.create_user(**validated_data)
                return user
            else:
                return Response({"Error": "User already Exist!"}, status=status.HTTP_409_CONFLICT)


class KPISerializer(serializers.Serializer):
    kpi_id = serializers.CharField(max_length = 120)
    objective = serializers.CharField(max_length=120)
    kpi_name = serializers.CharField(max_length=120)
    kpi_weight = serializers.FloatField()
    kpi_target = serializers.FloatField()
    perspective = serializers.CharField(max_length=120)
    kpi_unit_measurement = serializers.CharField(max_length=120)
    Score_January = serializers.FloatField()
    Score_February = serializers.FloatField()
    Score_March = serializers.FloatField()
    Score_April = serializers.FloatField()
    Score_May = serializers.FloatField()
    Score_June = serializers.FloatField()
    Score_July = serializers.FloatField()
    Score_August = serializers.FloatField()
    Score_September = serializers.FloatField()
    Score_October = serializers.FloatField()
    Score_November = serializers.FloatField()
    Score_December = serializers.FloatField()
    aggregate = serializers.FloatField()
    January = serializers.FloatField()
    February = serializers.FloatField()
    March = serializers.FloatField()
    April = serializers.FloatField()
    May = serializers.FloatField()
    June = serializers.FloatField()
    July = serializers.FloatField()
    August = serializers.FloatField()
    September = serializers.FloatField()
    October = serializers.FloatField()
    November = serializers.FloatField()
    December = serializers.FloatField()
    is_active = serializers.BooleanField()