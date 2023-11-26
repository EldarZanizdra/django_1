from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField()
    age = models.IntegerField()


class Admin(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)
    role = models.CharField(default='admin', max_length=5)


class Abstract(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    class Meta():
        abstract = True


class Project(Abstract):
    pass


class Task(Abstract):
    status = models.BooleanField()
    deadline = models.DateTimeField()
    priority = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
