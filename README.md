Employee Management System
This project is a web application built with Django and Django REST Framework to manage employee data within a company. The application provides API endpoints for creating, updating, deleting, and viewing data for employees, departments, attendance, and performance reviews.

Key Features
Full CRUD Functionality: APIs to manage Departments, Employees, Attendance records, and Performance reviews.

Interactive Documentation: A user-friendly Swagger UI for exploring and testing all API endpoints.

Automatic Data Seeding: A management command (seed_data) to populate the database with dummy data for easy testing.

Filtering & Searching: Ability to filter employees by department and joining date, and search by name or email.

Authentication: Token-based authentication to secure the API endpoints.

Data Visualization (Optional): A page to display charts for analyzing employee and attendance data.

Tech Stack
Backend: Django, Django REST Framework

Database: PostgreSQL (can be switched to SQLite for development)

API Documentation: drf-yasg (Swagger UI)

Environment Variables: django-environ

Dummy Data: Faker

Setup and Installation
Clone the repository:

git clone <your-repository-url>
cd employee_project_build

Create and activate a virtual environment:

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

Install the required packages:

pip install -r requirements.txt

Set up environment variables:

Copy the .env.example file to a new file named .env.

Fill in the required variables in the .env file (like SECRET_KEY and your PostgreSQL database credentials).

cp .env.example .env

Apply migrations:

python manage.py migrate

Create a superuser:

python manage.py createsuperuser

Seed the database with fake data:

python manage.py seed_data

Run the local development server:

python manage.py runserver

You can now access the project at http://127.0.0.1:8000.

API Usage
1. Obtain an Authentication Token
Go to the admin panel: http://127.0.0.1:8000/admin/

Log in with the superuser account you created.

In the "AUTHTOKEN" section, click on "Tokens".

Add a new token for your user and copy the generated key.

2. Access the Swagger UI
Navigate to http://127.0.0.1:8000/swagger/.

To test the endpoints, click the green "Authorize" button at the top right.

In the popup, enter Token followed by a space and your copied token. Example: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b.

3. Access the Charts Page
Before visiting the page, you need to store the token in your browser's local storage.

Open the Developer Tools in your browser (usually by pressing F12) and select the "Console" tab.

Paste the following command, replacing YOUR_TOKEN_HERE with your actual token:

localStorage.setItem('apiToken', 'YOUR_TOKEN_HERE');

Now, you can visit the charts page at http://127.0.0.1:8000/charts/.
