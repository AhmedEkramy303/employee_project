from django.db.models import Count, Q
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import TemplateView
from .models import Department, Employee, Attendance, Performance
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all(); serializer_class = DepartmentSerializer; permission_classes = [permissions.IsAuthenticated]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.select_related('department').all(); serializer_class = EmployeeSerializer; permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]; filterset_fields = ['department__name', 'date_of_joining']; search_fields = ['name', 'email']; ordering_fields = ['date_of_joining', 'name']

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.select_related('employee').all(); serializer_class = AttendanceSerializer; permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]; filterset_fields = ['employee__name', 'date', 'status']

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.select_related('employee').all(); serializer_class = PerformanceSerializer; permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]; filterset_fields = ['employee__name', 'rating', 'review_date']

class EmployeesPerDepartmentView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        data = Department.objects.annotate(employee_count=Count('employees')).values('name', 'employee_count')
        serializer = EmployeesPerDepartmentSerializer(data=[{'department': i['name'], 'employee_count': i['employee_count']} for i in data], many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

class MonthlyAttendanceView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        data = Attendance.objects.values('date').annotate(present_count=Count('status', filter=Q(status='Present')), absent_count=Count('status', filter=Q(status='Absent')), late_count=Count('status', filter=Q(status='Late'))).order_by('date')
        serializer = MonthlyAttendanceSerializer(data=list(data), many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

class ChartView(TemplateView): template_name = 'charts.html'