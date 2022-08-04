from django.contrib import admin
from .models import *

# Register your models here.

class PerspectiveAdmin(admin.ModelAdmin):
    list_display = (
        'perspective_id', 'perspective_name', 'perspective_weight',
    )

class ObjectiveAdmin(admin.ModelAdmin):
    list_display = (
        'objective_id', 'perspective', 'objective_name', 'objective_weight',
    )

admin.site.register(Perspective, PerspectiveAdmin)
admin.site.register(Objectives, ObjectiveAdmin)
admin.site.register(KPI)

