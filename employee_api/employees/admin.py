from django.contrib import admin
from .models import (Employee, MyUser, Department)


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position')
    search_fields = ('id', 'name', 'position')
    list_per_page = 25
    list_filter = ('id', 'name', 'position')
    ordering = ('id', 'name', 'position')
    list_editable = ('name', 'position')


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department')
    search_fields = ('id', 'name', 'email', 'department')
    list_per_page = 25
    list_filter = ('id', 'name', 'email', 'department')
    ordering = ('id', 'name', 'email', 'department')
    list_editable = ('name', 'email', 'department')

# admin.site.register(MyUser)


admin.site.register(Department)
