# 🏫 School Management System API

[![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-3.14-ff1709?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)](https://github.com/your-username/school-api)

A comprehensive RESTful API built with Django and Django REST Framework for managing a complete school system. This API provides full CRUD operations for students, teachers, and courses with advanced relational capabilities and robust data validation.

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Data Model](#️-data-model)
- [Quick Start](#-quick-start)
- [Installation](#️-installation--setup)
- [Configuration](#️-configuration)
- [API Documentation](#-api-documentation)
- [Usage Examples](#-usage-examples)
- [Authentication](#-authentication)
- [Testing](#-testing)
- [Admin Interface](#️-admin-interface)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [Troubleshooting](#-troubleshooting)
- [Changelog](#-changelog)
- [License](#-license)
- [Author](#-author)

## 🚀 Features

### Core Functionality
- ✅ **Student Management** - Complete CRUD operations with enrollment tracking
- ✅ **Teacher Management** - Staff records with subject specializations
- ✅ **Course Management** - Course creation with student/teacher assignments
- ✅ **Enrollment System** - Many-to-many relationships for flexible course assignments
- ✅ **Grade Tracking** - Student performance monitoring
- ✅ **RESTful API Design** - Industry-standard REST architecture

### Technical Features
- 🔐 **Authentication & Authorization** - Token-based security
- 📊 **Data Validation** - Comprehensive input validation
- 🔍 **Search & Filtering** - Advanced query capabilities
- 📄 **Pagination** - Efficient data loading
- 📖 **API Documentation** - Auto-generated OpenAPI/Swagger docs
- 🧪 **Unit Testing** - Comprehensive test coverage
- 🐳 **Docker Support** - Containerized deployment ready
- 📈 **Performance Optimized** - Database query optimization

## 🏗 Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   API Gateway   │    │   Database      │
│   (React/Vue)   │◄──►│   Django REST   │◄──►│   PostgreSQL    │
│                 │    │   Framework     │    │   /SQLite       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │   Admin Panel   │
                    │   Django Admin  │
                    └─────────────────┘
```

## 🗄️ Data Model

```mermaid
erDiagram
    STUDENT {
        int id PK
        string first_name
        string last_name
        int age
        float grade
        datetime created_at
        datetime updated_at
    }
    
    TEACHER {
        int id PK
        string name
        string subject
        string email
        string phone
        datetime created_at
        datetime updated_at
    }
    
    COURSE {
        int id PK
        string title
        string description
        int credits
        string semester
        datetime created_at
        datetime updated_at
    }
    
    ENROLLMENT {
        int id PK
        int student_id FK
        int course_id FK
        datetime enrollment_date
        float grade
        string status
    }
    
    COURSE_TEACHER {
        int id PK
        int course_id FK
        int teacher_id FK
        string role
    }
    
    STUDENT ||--o{ ENROLLMENT : "enrolls in"
    COURSE ||--o{ ENROLLMENT : "has enrolled"
    TEACHER ||--o{ COURSE_TEACHER : "teaches"
    COURSE ||--o{ COURSE_TEACHER : "taught by"
```

## ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/ezzmasre/school-management-api.git
cd school-management-api

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up database
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/api/` to access the API!

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ezzmasre/school-management-api.git
   cd school-management-api
   ```

2. **Create Virtual Environment**
   ```bash
   # Create virtual environment
   python -m venv school_env
   
   # Activate virtual environment
   # On Windows:
   school_env\Scripts\activate
   
   # On macOS/Linux:
   source school_env/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   # Install required packages
   pip install -r requirements.txt
   
   # Or install manually:
   pip install django==4.2
   pip install djangorestframework==3.14
   pip install django-cors-headers
   pip install django-filter
   pip install drf-spectacular
   ```

4. **Environment Configuration**
   ```bash
   # Copy environment template
   cp .env.example .env
   
   # Edit .env file with your settings
   nano .env
   ```

5. **Database Setup**
   ```bash
   # Create and apply migrations
   python manage.py makemigrations
   python manage.py migrate
   
   # Load sample data (optional)
   python manage.py loaddata fixtures/sample_data.json
   ```

6. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DATABASE_URL=sqlite:///db.sqlite3
# For PostgreSQL:
# DATABASE_URL=postgres://user:password@localhost:5432/school_db

# API Configuration
API_VERSION=v1
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# Email Configuration (for notifications)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Settings Configuration

Key settings in `settings.py`:

```python
# API Settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}
```

## 📚 API Documentation

### Interactive API Documentation

- **Swagger UI**: `http://127.0.0.1:8000/api/docs/`
- **ReDoc**: `http://127.0.0.1:8000/api/redoc/`
- **OpenAPI Schema**: `http://127.0.0.1:8000/api/schema/`

### Endpoint Overview

| Resource | Endpoint | Methods | Description |
|----------|----------|---------|-------------|
| **Students** | `/api/v1/students/` | GET, POST | List all students, create new student |
| | `/api/v1/students/{id}/` | GET, PUT, PATCH, DELETE | Retrieve, update, delete student |
| | `/api/v1/students/search/` | GET | Search students by name or grade |
| **Teachers** | `/api/v1/teachers/` | GET, POST | List all teachers, create new teacher |
| | `/api/v1/teachers/{id}/` | GET, PUT, PATCH, DELETE | Retrieve, update, delete teacher |
| | `/api/v1/teachers/{id}/courses/` | GET | Get courses taught by teacher |
| **Courses** | `/api/v1/courses/` | GET, POST | List all courses, create new course |
| | `/api/v1/courses/{id}/` | GET, PUT, PATCH, DELETE | Retrieve, update, delete course |
| | `/api/v1/courses/{id}/students/` | GET, POST | Manage course enrollments |
| | `/api/v1/courses/{id}/teachers/` | GET, POST | Manage course instructors |
| **Enrollments** | `/api/v1/enrollments/` | GET, POST | List enrollments, create enrollment |
| | `/api/v1/enrollments/{id}/` | GET, PUT, PATCH, DELETE | Manage specific enrollment |
| **Authentication** | `/api/v1/auth/login/` | POST | User login |
| | `/api/v1/auth/logout/` | POST | User logout |
| | `/api/v1/auth/register/` | POST | User registration |

### Query Parameters

All list endpoints support:

- **Pagination**: `?page=1&page_size=20`
- **Filtering**: `?grade__gte=80&age__lt=25`
- **Search**: `?search=alice`
- **Ordering**: `?ordering=-created_at,name`

## 💻 Usage Examples

### Authentication

```bash
# Login to get token
curl -X POST http://127.0.0.1:8000/api/v1/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "password123"}'

# Response
{
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b",
  "user": {
    "id": 1,
    "username": "admin",
    "email": "admin@example.com"
  }
}

# Use token in subsequent requests
curl -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" \
  http://127.0.0.1:8000/api/v1/students/
```

### Student Operations

#### Create a Student
```bash
curl -X POST http://127.0.0.1:8000/api/v1/students/ \
  -H "Authorization: Token your-token-here" \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Alice",
    "last_name": "Johnson", 
    "age": 20,
    "grade": 85.5,
    "email": "alice.johnson@student.edu"
  }'
```

**Response:**
```json
{
  "id": 1,
  "first_name": "Alice",
  "last_name": "Johnson",
  "age": 20,
  "grade": 85.5,
  "email": "alice.johnson@student.edu",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z",
  "courses": []
}
```

#### List Students with Filtering
```bash
# Get students with grade above 80
curl "http://127.0.0.1:8000/api/v1/students/?grade__gte=80&ordering=-grade" \
  -H "Authorization: Token your-token-here"
```

#### Update a Student
```bash
curl -X PATCH http://127.0.0.1:8000/api/v1/students/1/ \
  -H "Authorization: Token your-token-here" \
  -H "Content-Type: application/json" \
  -d '{"grade": 90.0}'
```

### Teacher Operations

#### Create a Teacher
```bash
curl -X POST http://127.0.0.1:8000/api/v1/teachers/ \
  -H "Authorization: Token your-token-here" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Dr. Sarah Wilson",
    "subject": "Mathematics",
    "email": "s.wilson@school.edu",
    "phone": "+1-555-0123"
  }'
```

### Course Operations

#### Create a Course
```bash
curl -X POST http://127.0.0.1:8000/api/v1/courses/ \
  -H "Authorization: Token your-token-here" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Advanced Calculus",
    "description": "Advanced mathematical concepts and applications",
    "credits": 4,
    "semester": "Fall 2024"
  }'
```

#### Enroll Student in Course
```bash
curl -X POST http://127.0.0.1:8000/api/v1/courses/1/students/ \
  -H "Authorization: Token your-token-here" \
  -H "Content-Type: application/json" \
  -d '{"student_id": 1}'
```

### Python Client Examples

```python
import requests
import json

class SchoolAPIClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Token {token}',
            'Content-Type': 'application/json'
        }
    
    def create_student(self, student_data):
        response = requests.post(
            f'{self.base_url}/students/',
            headers=self.headers,
            json=student_data
        )
        return response.json()
    
    def get_student(self, student_id):
        response = requests.get(
            f'{self.base_url}/students/{student_id}/',
            headers=self.headers
        )
        return response.json()
    
    def enroll_student(self, course_id, student_id):
        response = requests.post(
            f'{self.base_url}/courses/{course_id}/students/',
            headers=self.headers,
            json={'student_id': student_id}
        )
        return response.json()

# Usage
client = SchoolAPIClient('http://127.0.0.1:8000/api/v1', 'your-token')

# Create a student
student = client.create_student({
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 19,
    'grade': 88.0
})

print(f"Created student: {student['first_name']} {student['last_name']}")
```

## 🔐 Authentication

The API uses Token-based authentication. Here's how to work with it:

### Getting a Token

```python
import requests

response = requests.post('http://127.0.0.1:8000/api/v1/auth/login/', {
    'username': 'your_username',
    'password': 'your_password'
})

if response.status_code == 200:
    token = response.json()['token']
    print(f"Token: {token}")
```

### Using the Token

Include the token in the Authorization header:

```python
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/v1/students/', headers=headers)
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific test module
python manage.py test apps.students.tests

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report
```

### Test Structure

```
tests/
├── test_models.py      # Model tests
├── test_views.py       # API endpoint tests
├── test_serializers.py # Serializer tests
└── fixtures/
    └── test_data.json  # Test data
```

### Example Test Case

```python
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from apps.students.models import Student

class StudentAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
    
    def test_create_student(self):
        data = {
            'first_name': 'Test',
            'last_name': 'Student',
            'age': 20,
            'grade': 85.0
        }
        response = self.client.post('/api/v1/students/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 1)
```

## 🖥️ Admin Interface

### Accessing the Admin Panel

1. Create a superuser: `python manage.py createsuperuser`
2. Visit: `http://127.0.0.1:8000/admin/`
3. Login with your superuser credentials

### Admin Features

- **Student Management**: View, edit, and delete student records
- **Teacher Management**: Manage teacher profiles and assignments
- **Course Administration**: Create and manage courses
- **Enrollment Tracking**: Monitor student enrollments
- **User Management**: Manage API users and permissions
- **System Logs**: View API usage and error logs

### Custom Admin Actions

- **Bulk Operations**: Update multiple records at once
- **Export Data**: Download data as CSV/Excel
- **Email Notifications**: Send bulk emails to students/teachers
- **Report Generation**: Generate academic reports

## 🚀 Deployment

### Docker Deployment

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - DATABASE_URL=postgres://user:password@db:5432/school_db
    depends_on:
      - db
  
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: school_db
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### Production Deployment

1. **Heroku Deployment**
   ```bash
   # Install Heroku CLI and login
   heroku create your-school-api
   heroku config:set DEBUG=False
   heroku config:set SECRET_KEY=your-production-secret-key
   git push heroku main
   heroku run python manage.py migrate
   ```

2. **AWS EC2 Deployment**
   ```bash
   # Install dependencies
   sudo apt update
   sudo apt install python3-pip nginx gunicorn
   
   # Configure Gunicorn
   gunicorn --bind 0.0.0.0:8000 school_api.wsgi:application
   
   # Configure Nginx
   sudo nano /etc/nginx/sites-available/school_api
   ```

### Environment-Specific Settings

```python
# settings/production.py
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

# Security settings
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup

```bash
# Fork the repository and clone your fork
git clone https://github.com/your-username/school-management-api.git
cd school-management-api

# Create a feature branch
git checkout -b feature/your-feature-name

# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

### Contribution Guidelines

1. **Code Style**
   - Follow PEP 8 conventions
   - Use Black for code formatting: `black .`
   - Use isort for import sorting: `isort .`
   - Run flake8 for linting: `flake8 .`

2. **Testing**
   - Write tests for new features
   - Ensure all tests pass: `python manage.py test`
   - Maintain test coverage above 90%

3. **Documentation**
   - Update README for new features
   - Add docstrings to new functions/classes
   - Update API documentation

4. **Pull Request Process**
   - Create a detailed PR description
   - Link to related issues
   - Ensure CI/CD passes
   - Request review from maintainers

### Development Tools

```bash
# Install development dependencies
pip install black isort flake8 pre-commit pytest-django

# Set up pre-commit hooks
pre-commit install

# Run formatting
black .
isort .

# Run linting
flake8 .

# Run tests with pytest
pytest
```

## 🔧 Troubleshooting

### Common Issues

#### Database Connection Errors
```bash
# Check database connection
python manage.py dbshell

# Reset migrations
python manage.py migrate --fake-initial

# Create new migration
python manage.py makemigrations --empty your_app_name
```

#### Authentication Issues
```python
# Check token validity
from rest_framework.authtoken.models import Token
token = Token.objects.get(key='your-token')
print(token.user.username)
```

#### CORS Issues
```python
# Add to settings.py
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

CORS_ALLOW_ALL_ORIGINS = True  # Only for development
```

### Debug Mode

Enable debug mode for development:

```python
# settings.py
DEBUG = True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
```

### Performance Issues

```python
# Add database query optimization
from django.db import connection
from django.conf import settings

if settings.DEBUG:
    print(f"Database queries: {len(connection.queries)}")
    for query in connection.queries:
        print(query['sql'])
```

## 📝 Changelog

### Version 2.1.0 (2024-01-15)
- ✨ Added course enrollment system
- 🔐 Implemented token authentication
- 📊 Added advanced filtering and search
- 🐛 Fixed grade calculation bugs
- 📚 Enhanced API documentation

### Version 2.0.0 (2023-12-01)
- 🎉 Major API redesign
- ⚡ Performance improvements
- 🧪 Added comprehensive test suite
- 🐳 Docker support
- 📱 Mobile-friendly admin interface

### Version 1.5.0 (2023-10-15)
- ✅ Added teacher management
- 🔍 Implemented search functionality
- 📄 Added pagination support
- 🛡️ Enhanced security measures

### Version 1.0.0 (2023-09-01)
- 🚀 Initial release
- 👥 Basic student CRUD operations
- 📚 Course management
- 🖥️ Admin interface

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 👨‍💻 Author

**Your Name** - *Full Stack Developer*

- 🌐 Website: [yourwebsite.com](https://yourwebsite.com)
- 💼 LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
- 🐙 GitHub: [@your-github-username](https://github.com/your-github-username)
- 📧 Email: your.email@domain.com
- 🐦 Twitter: [@yourtwitterhandle](https://twitter.com/yourtwitterhandle)

### 🤝 Connect With Me

- 💬 Open for collaboration on Django/Python projects
- 📫 Feel free to reach out for questions or suggestions
- ⭐ If you found this project helpful, please give it a star!

---

<div align="center">

**Made with ❤️ and Django**

[![Stars](https://img.shields.io/github/stars/your-username/school-management-api?style=social)](https://github.com/your-username/school-management-api/stargazers)
[![Forks](https://img.shields.io/github/forks/your-username/school-management-api?style=social)](https://github.com/your-username/school-management-api/network/members)
[![Issues](https://img.shields.io/github/issues/your-username/school-management-api)](https://github.com/your-username/school-management-api/issues)

</div>
