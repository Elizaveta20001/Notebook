from django.db import models


class Note(models.Model):
    text = models.CharField(max_length=1000)


class Person(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    notes = models.ForeignKey(Note,on_delete=models.CASCADE)


# Create your models here.
