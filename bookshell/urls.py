from django.urls import path
 
from .views import MyListView
 
urlpatterns = [
    #path('post/<int:pk>/', bookDetailView.as_view(), name='post_detail'),
    path('', MyListView, name='home'),
]