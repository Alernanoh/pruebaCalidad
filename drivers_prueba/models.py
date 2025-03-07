from django.db import models

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

def __str__(self):
    return self.name
