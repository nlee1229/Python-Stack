from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('book', views.addbook),
    path('viewbook/<id>', views.book_info),
    path('author_add', views.author_adding),
    # author index3
    path('author', views.author_info),
    path('author/add_an_author', views.add_an_author),
    path('viewauthor/<id>', views.author_page),
    path('book_add', views.book_adding),

    
    

]
