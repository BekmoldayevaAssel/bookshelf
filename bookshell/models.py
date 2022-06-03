from django.db import models

# Create your models here.
class Authors(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    data_of_birth = models.DateField()
    author_info = models.CharField(max_length=300)

class company(models.Model):
    title = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    language = models.CharField(max_length=50)


class genres(models.Model):
     title = models.CharField(max_length=100)   