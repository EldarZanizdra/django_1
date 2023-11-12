from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)


class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(upload_to='static/images')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Users(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField()
    age = models.IntegerField()


class Artist(models.Model):
    name = models.CharField(max_length=30)
    year = models.DateTimeField()


class Albums(models.Model):
    title = models.CharField(max_length=100)
    year = models.DateTimeField()
    poster = models.ImageField(upload_to='static/images')
    singer = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Instruments(models.Model):
    name = models.CharField(max_length=60)


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=6)
    date_of_birth = models.DateTimeField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instruments, on_delete=models.CASCADE)


class Directors(models.Model):
    first_name = models.CharField(max_length=60)
    second_name = models.CharField(max_length=60)
    age = models.IntegerField()


class Films(models.Model):
    title = models.CharField(max_length=100)
    year = models.DateField()
    director = models.ForeignKey(Directors, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)
    # poster = models.ImageField()