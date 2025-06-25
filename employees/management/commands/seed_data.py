import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Department, Employee, Attendance, Performance

class Command(BaseCommand):
    help = 'Seeds the database with fake data.'
    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database...")
        fake = Faker()
        Performance.objects.all().delete()
        Attendance.objects.all().delete()
        Employee.objects.all().delete()
        Department.objects.all().delete()
        departments = ['HR', 'Engineering', 'Marketing', 'Sales', 'Finance']
        dept_objects = [Department.objects.create(name=d) for d in departments]
        employee_objects = [Employee.objects.create(name=fake.name(), email=fake.unique.email(), phone_number=fake.phone_number(), address=fake.address(), date_of_joining=fake.date_between(start_date='-5y', end_date='today'), department=random.choice(dept_objects)) for _ in range(50)]
        today = date.today()
        for employee in employee_objects:
            for i in range(30):
                current_date = today - timedelta(days=i)
                Attendance.objects.create(employee=employee, date=current_date, status=random.choice(['Present', 'Present', 'Absent', 'Late']))
                if current_date.day == 15:
                    Performance.objects.create(employee=employee, rating=random.randint(1, 5), review_date=current_date)
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database!'))