# 🏫 School Management System API (Django REST Framework)

A comprehensive RESTful API built with Django and Django REST Framework for managing a school system. This API supports CRUD operations for students, teachers, and courses with relational capabilities.

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![DRF](https://img.shields.io/badge/Django_REST-Framework-red?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 📋 Table of Contents

- [Features](#-features)
- [Data Model](#-data-model)
- [Installation & Setup](#-installation--setup)
- [API Endpoints](#-api-endpoints)
- [Usage Examples](#-usage-examples)
- [Admin Interface](#-admin-interface)
- [Contributing](#-contributing)
- [Author](#-author)

---

## 🚀 Features

- **Student Management**
  - Create, read, update, and delete student records
  - Fields: First Name, Last Name, Age, Grade

- **Teacher Management**
  - Create, read, update, and delete teacher records
  - Fields: Name, Subject

- **Course Management**
  - Create, read, update, and delete courses
  - Assign students and teachers to courses
  - Many-to-Many relationships between courses and students/teachers

- **RESTful Design**
  - Proper HTTP status codes
  - JSON request/response format
  - Resource-based URL structure

---

## 🗄️ Data Model

```plaintext
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
نسخ الكود
git clone https://github.com/your-username/school-api.git
cd school-api
Create and activate a virtual environment

bash
نسخ الكود
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Install dependencies

bash
نسخ الكود
pip install django djangorestframework
Apply migrations

bash
نسخ الكود
python manage.py makemigrations
python manage.py migrate
Create a superuser (optional, for admin access)

bash
نسخ الكود
python manage.py createsuperuser
Start the development server

bash
نسخ الكود
python manage.py runserver
🌐 API Endpoints
Resource	URL	Method	Description
Students	/api/students/	GET	List all students
Students	/api/students/	POST	Create a new student
Students	/api/students/{id}/	GET	Retrieve student details
Students	/api/students/{id}/	PUT	Update student
Students	/api/students/{id}/	DELETE	Delete student
Teachers	/api/teachers/	GET/POST	CRUD for teachers
Courses	/api/courses/	GET/POST	CRUD for courses

All data is returned in JSON format.

🧑‍💻 Usage Examples
Add a student (POST /api/students/):

json
نسخ الكود
{
  "first_name": "Alice",
  "last_name": "Johnson",
  "age": 20,
  "grade": 85
}
Response:

json
نسخ الكود
{
  "id": 1,
  "first_name": "Alice",
  "last_name": "Johnson",
  "age": 20,
  "grade": 85
}
Get all students (GET /api/students/):

json
نسخ الكود
[
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
    "last_name": "Smith",
    "age": 19,
    "grade": 90
  }
]
🏢 Admin Interface
Access the admin panel at /admin/

Requires superuser credentials created during setup

🤝 Contributing
Fork the repository

Create a new branch: git checkout -b feature-name

Make your changes

Commit: git commit -m 'Add feature'

Push to the branch: git push origin feature-name

Create a pull request

🛡️ Author
Your Name (@your-github-username)

🏷️ Badges



yaml
نسخ الكود

---

If you want, I can also **make a version with Mermaid.js diagrams** so GitHub renders a **real graphical diagram** for Student ↔ Course ↔ Teacher relationships — looks way more professional than ASCII.  

Do you want me to do that next?
