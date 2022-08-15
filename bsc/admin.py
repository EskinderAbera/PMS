from django.contrib import admin
from .models import *

# Register your models here.

class PerspectiveAdmin(admin.ModelAdmin):
    list_display = (
        'perspective_id', 'perspective_name', 'perspective_weight',
    )
    search_fields = ("perspective_name", "perspective_id", "user__id")

class ObjectiveAdmin(admin.ModelAdmin):
    list_display = (
        'objective_id', 'perspective', 'objective_name', 'objective_weight',
    )
    search_fields = ("objective_name", "objective_id", "user__id")

class KPIAdmin(admin.ModelAdmin):
    list_display = (
        'kpi_id', 'perspective', 'objective', 'kpi_name'
    )
    search_fields = ("kpi_id", "kpi_name", "user__id")

admin.site.register(Perspective, PerspectiveAdmin)
admin.site.register(Objectives, ObjectiveAdmin)
admin.site.register(KPI, KPIAdmin)

