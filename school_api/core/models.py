from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    grade = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=50)
    students = models.ManyToManyField(Student, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
