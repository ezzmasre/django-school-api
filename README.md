🏫 School Management System API (Django REST Framework)
A comprehensive RESTful API built with Django and Django REST Framework for managing a school system. This API supports CRUD operations for students, teachers, and courses with relational capabilities.

https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
https://img.shields.io/badge/Django_REST-Framework-red?style=for-the-badge
https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white

📋 Table of Contents
Features

Data Model

Installation & Setup

API Endpoints

Usage Examples

Admin Interface

Contributing

Author

🚀 Features
Student Management

Create, read, update, and delete student records

Fields: First Name, Last Name, Age, Grade

Teacher Management

Create, read, update, and delete teacher records

Fields: Name, Subject

Course Management

Create, read, update, and delete courses

Assign students and teachers to courses

Many-to-Many relationships between courses and students/teachers

RESTful Design

Proper HTTP status codes

JSON request/response format

Resource-based URL structure

🗄️ Data Model
plaintext
+----------+       +---------+       +----------+
| Teacher  |       | Course  |       | Student  |
+----------+       +---------+       +----------+
| id       |1    * | id      |*     *| id       |
| name     |-------| title   |-------| first_name|
| subject  |       | teacher |       | last_name |
+----------+       | students|       | age      |
                   +---------+       | grade    |
                                     +----------+
🛠️ Installation & Setup
Clone the repository

bash
git clone https://github.com/your-username/school_api.git
cd school_api
Create and activate a virtual environment

bash
# Using virtualenv
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
Install dependencies

bash
pip install django djangorestframework
Apply migrations

bash
python manage.py makemigrations
python manage.py migrate
Create a superuser (optional, for admin access)

bash
python manage.py createsuperuser
Start the development server

bash
python manage.py runserver
The API will be available at http://localhost:8000/

📊 API Endpoints
Students
Method	Endpoint	Description
GET	/api/students/	List all students
POST	/api/students/	Create a new student
GET	/api/students/{id}/	Retrieve a specific student
PUT	/api/students/{id}/	Update a student
PATCH	/api/students/{id}/	Partially update a student
DELETE	/api/students/{id}/	Delete a student
Teachers
Method	Endpoint	Description
GET	/api/teachers/	List all teachers
POST	/api/teachers/	Create a new teacher
GET	/api/teachers/{id}/	Retrieve a specific teacher
PUT	/api/teachers/{id}/	Update a teacher
PATCH	/api/teachers/{id}/	Partially update a teacher
DELETE	/api/teachers/{id}/	Delete a teacher
Courses
Method	Endpoint	Description
GET	/api/courses/	List all courses
POST	/api/courses/	Create a new course
GET	/api/courses/{id}/	Retrieve a specific course
PUT	/api/courses/{id}/	Update a course
PATCH	/api/courses/{id}/	Partially update a course
DELETE	/api/courses/{id}/	Delete a course
💻 Usage Examples
Create a Student (POST /api/students/)
Request:

bash
curl -X POST http://localhost:8000/api/students/ \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Alice",
    "last_name": "Johnson",
    "age": 20,
    "grade": 85
  }'
Response:

json
{
  "id": 1,
  "first_name": "Alice",
  "last_name": "Johnson",
  "age": 20,
  "grade": 85
}
Create a Course with Teacher and Students (POST /api/courses/)
Request:

bash
curl -X POST http://localhost:8000/api/courses/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Mathematics 101",
    "teacher": 1,
    "students": [1, 2, 3]
  }'
Response:

json
{
  "id": 1,
  "title": "Mathematics 101",
  "teacher": {
    "id": 1,
    "name": "Dr. Smith",
    "subject": "Mathematics"
  },
  "students": [
    {
      "id": 1,
      "first_name": "Alice",
      "last_name": "Johnson",
      "age": 20,
      "grade": 85
    },
    {
      "id": 2,
      "first_name": "Bob",
      "last_name": "Williams",
      "age": 19,
      "grade": 78
    },
    {
      "id": 3,
      "first_name": "Charlie",
      "last_name": "Brown",
      "age": 21,
      "grade": 92
    }
  ]
}
👨‍💼 Admin Interface
The Django admin interface is available at /admin/ after creating a superuser. This provides a graphical interface to manage all data models.

🤝 Contributing
Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add some amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

🛡️ Author
Your Name - @your-github-username

📝 Notes
Make sure to run the server in the virtual environment where Django is installed

Use tools like Postman, curl, or HTTPie to test the API endpoints

The admin panel provides an alternative way to manage data at /admin/
