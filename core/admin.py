from django.contrib import admin
from .models import Sub_SubDepartment, User, Department, Role, SubDepartment

# Register your models here.

class UserAdmins(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'department', 'subdepartment', 'role')
    search_fields = ("username", "id", "first_name")
    readonly_fields = ('date_joined', 'last_login')

admin.site.register(User, UserAdmins)
admin.site.register(Department)
admin.site.register(SubDepartment)
admin.site.register(Role)
admin.site.register(Sub_SubDepartment)
