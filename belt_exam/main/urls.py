from django.urls import path
from . import views

urlpatterns = [
	path('books', views.index),
	path('books/newtrip', views.newtrip),
	path('books/new_trip', views.addtrip),
	path('books/<int:id>/remove', views.remove),
	path('books/<int:id>/edit', views.edit),
	path('books/<int:id>/update', views.update),
	path('books/<int:id>/view', views.view),
	
]