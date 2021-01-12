from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('dojo', views.dojo_add),
    path('add_ninja', views.ninja_add),
    path('delete', views.delete_info),
]