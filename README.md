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


---

## 🔗 Relationships Diagram

```text
          +-----------+
          |  Teacher  |
          |-----------|
          | name      |
          | subject   |
          +-----------+
                |
                | teaches
                v
          +-----------+
          |  Course   |
          |-----------|
          | name      |
          | teacher   |
          +-----------+
          ^       ^
          |       | enrolled in
          |       |
    +-----------+  +-----------+
    | Student   |  | Student   |
    |-----------|  |-----------|
    | first_name|  | first_name|
    | last_name |  | last_name |
    | age       |  | age       |
    | grade     |  | grade     |
    +-----------+  +-----------+
Clone the repository:
git clone https://github.com/your-username/school-api.git
cd school-api
Create and activate a virtual environment:
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
