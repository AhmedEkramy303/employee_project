from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'performance', PerformanceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/charts/employees-per-department/', EmployeesPerDepartmentView.as_view()),
    path('api/charts/monthly-attendance/', MonthlyAttendanceView.as_view()),
    path('charts/', ChartView.as_view(), name='charts-page'),
]