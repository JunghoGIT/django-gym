from django.db import models


class Person(models.Model):

    name = models.CharField(max_length=30, unique=True)
    age = models.IntegerField()


class Animal(models.Model):

    owner = models.ForeignKey('Person', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True)


class Nothing(models.Model):

    contents = models.TextField()

