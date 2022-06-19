from ast import Return
from turtle import title
from django.db import models

# Create your models here.
class Authors(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    data_of_birth = models.DateField()
    author_info = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class company(models.Model):
    title = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.title



class genres(models.Model):
     title = models.CharField(max_length=100) 

     def __str__(self):
        return self.title  

class books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('bookshell.Authors', on_delete=models.CASCADE)
    company = models.ForeignKey('bookshell.company', on_delete=models.CASCADE)
    genres = models.ForeignKey('bookshell.genres', on_delete=models.CASCADE)
    year = models.IntegerField()
    page = models.IntegerField()
    book_info = models.CharField(max_length=300)
   
    def __str__(self):
        return self.title

