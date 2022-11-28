from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField() 
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name       


# Create your models here.
