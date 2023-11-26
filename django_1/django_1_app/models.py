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


class Group(models.Model):
    class_number = models.IntegerField()


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    student_card_number = models.IntegerField()


class Card(models.Model):
    date_of_issue = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Literature(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    date_of_publication = models.DateTimeField()


class Borrowing_a_book(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    title_of_the_book = models.ForeignKey(Literature, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
