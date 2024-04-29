from rest_framework import serializers
from .models import Employee, MyUser, Department


# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ['id', 'name', 'position']
        
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    users = MyUserSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = '__all__'