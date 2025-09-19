# 🏫 School Management System API (Django REST Framework)

This is a **RESTful API** built with **Django** and **Django REST Framework** to manage a school system.  
It allows you to perform **CRUD operations** on students, teachers, and courses.

---

## 🚀 Features

- **Students**
  - Add, view, update, and delete students
  - Fields: First Name, Last Name, Age, Grade

- **Teachers**
  - Add, view, update, and delete teachers
  - Fields: Name, Subject

- **Courses**
  - Add, view, update, and delete courses
  - Assign students and teachers to courses

- Demonstrates **Object-Oriented Programming** and **Django REST Framework** principles

---

## 🛠️ Project Structure

school_api/
│── manage.py
│── school_api/ # Django project settings
│ │── settings.py
│ │── urls.py
│── core/ # Django app
│── models.py
│── serializers.py
│── views.py
│── urls.py

---

## ▶️ Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/school_api.git
cd school_api
Create and activate a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Install dependencies:

pip install django djangorestframework

Apply migrations:

python manage.py makemigrations
python manage.py migrate

Create a superuser (optional, for admin access):

python manage.py createsuperuser


Start the development server:

python manage.py runserver

API Endpoints
Resource	URL	Method	Description
Students	/api/students/	GET	List all students
Students	/api/students/	POST	Create a new student
Students	/api/students/{id}/	GET	Retrieve student details
Students	/api/students/{id}/	PUT	Update student
Students	/api/students/{id}/	DELETE	Delete student
Teachers	/api/teachers/	GET/POST	CRUD for teachers
Courses	/api/courses/	GET/POST	CRUD for courses

All data is returned in JSON format.

🧑‍💻 Usage Example

Add a student (POST /api/students/):

{
  "first_name": "Alice",
  "last_name": "Johnson",
  "age": 20,
  "grade": 85
}


Response:

{
  "id": 1,
  "first_name": "Alice",
  "last_name": "Johnson",
  "age": 20,
  "grade": 85
}

🛡️ Author

Your Name (@your-github-username)

⚡ Notes

Make sure to run the server in the virtual environment where Django is installed.

You can use Postman or curl to test the API endpoints.

Admin panel available at /admin/ after creating a superuser.


---

If you want, I can also make a **more visual README** with **diagrams for Student ↔ Course ↔ Teacher** relationships and example API responses. That makes it look professional on GitHub.  

Do you want me to do that?
