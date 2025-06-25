from rest_framework import serializers
from .models import Department, Employee, Attendance, Performance

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta: model = Department; fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()
    class Meta: model = Employee; fields = ('id', 'name', 'email', 'phone_number', 'address', 'date_of_joining', 'department')

class AttendanceSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()
    class Meta: model = Attendance; fields = ('id', 'employee', 'date', 'status')

class PerformanceSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()
    class Meta: model = Performance; fields = ('id', 'employee', 'rating', 'review_date')

class EmployeesPerDepartmentSerializer(serializers.Serializer):
    department = serializers.CharField(); employee_count = serializers.IntegerField()

class MonthlyAttendanceSerializer(serializers.Serializer):
    date = serializers.DateField(); present_count = serializers.IntegerField(); absent_count = serializers.IntegerField(); late_count = serializers.IntegerField()