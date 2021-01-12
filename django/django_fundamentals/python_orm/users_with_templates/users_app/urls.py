from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('newdata', views.data),
	path('delete', views.delete),
]