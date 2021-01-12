from django.urls import path
from . import views

urlpatterns = [
	path('books', views.index),
	path('books/add', views.addbook),
]