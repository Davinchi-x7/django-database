from django.db import models



class Student(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    email = models.EmailField(max_length=50, blank=True, null=False)
    age = models.IntegerField(blank=True, null=False)
    gender = models.CharField(max_length=50, blank=True, null=False)
    phone = models.CharField(max_length=10, blank=True, null=False)
    city = models.CharField(max_length=50, blank=True, null=False)
    country = models.CharField(max_length=50, blank=True, null=False)

def __str__(self):
    return self.name
