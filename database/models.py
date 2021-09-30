from django.db import models


class Details(models.Model):
    name = models.CharField(max_length=255)
    bloodgroup = models.CharField(max_length=100)
    age = models.IntegerField()