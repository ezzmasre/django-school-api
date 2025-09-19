from django.urls import path, include
from rest_framework import routers
from .views import StudentViewSet, TeacherViewSet, CourseViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
