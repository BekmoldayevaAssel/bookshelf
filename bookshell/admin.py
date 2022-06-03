from django.contrib import admin
from .models import books, Authors, genres, company

# Register your models here.
admin.site.register(books)
admin.site.register(Authors)
admin.site.register(genres)
admin.site.register(company)
