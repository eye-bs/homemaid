from django.db import models


class Maid(models.Model):
    name = models.CharField(max_length=300)
    profile_image = models.FileField()
    birthdate = models.DateField()
    certificate = models.TextField()
    description = models.TextField()
    salary = models.IntegerField()