from django.db import models

# Create your models here
class Admin(models.Model):
    username = models.TextField()
    password = models.TextField()