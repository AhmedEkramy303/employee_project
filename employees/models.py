from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self): return self.name

class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    date_of_joining = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    def __str__(self): return self.name

class Attendance(models.Model):
    STATUS_CHOICES = (('Present', 'Present'), ('Absent', 'Absent'), ('Late', 'Late'))
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    class Meta: unique_together = ('employee', 'date')
    def __str__(self): return f"{self.employee.name} - {self.date} - {self.status}"

class Performance(models.Model):
    RATING_CHOICES = ((1, '1-Poor'), (2, '2-Fair'), (3, '3-Average'), (4, '4-Good'), (5, '5-Excellent'))
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performance')
    rating = models.IntegerField(choices=RATING_CHOICES)
    review_date = models.DateField()
    def __str__(self): return f"{self.employee.name} - Rating: {self.rating}"