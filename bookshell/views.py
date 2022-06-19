from contextvars import Context
from django.shortcuts import render
from django.views.generic import ListView
from .models import Authors, company, genres, books  

 
class BookListView(ListView):
    model = books
    template_name = 'home.html'

#class bookDetailView(DetailView):
   # model = Post
    #template_name = 'post_detail.html'

def MyListView(request):
    genreList = genres.objects.all()
    template_name ='Home.html'
    AuthorsList = Authors.objects.all()
    companyList = company.objects.all()
    context = {'genres': genreList, 'authors': AuthorsList, 'company': companyList}
    return render(request, 'Home.html', context)
