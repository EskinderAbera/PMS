from dataclasses import fields
from pyexpat import model
from .models import KPI, Objectives, Perspective
from rest_framework import serializers

class PerspectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perspective
        fields = '__all__'

class ObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objectives
        fields = '__all__'
    
class KPISerializer(serializers.ModelSerializer):
    class Meta:
        model = KPI
        fields = '__all__'


class AddKPISerializer(serializers.ModelSerializer):
    class Meta:
        model = KPI
        fields = ['kpi_id','kpi_name', 'kpi_weight', 'kpi_target', 'perspective', 'objective', 'kpi_unit_measurement', 'user']

class AddActualKPISerializer(serializers.ModelSerializer):
    class Meta:
        model = KPI
        fields = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']



class CreateKPISerializer(serializers.ModelSerializer):
    class Meta:
        model = KPI
        fields = ['kpi_id', 'kpi_name', 'kpi_weight', 'kpi_target', 'perspective', 'objective', 'kpi_unit_measurement', 'user' ]