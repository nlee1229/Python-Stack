from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('process', views.add),
    path('delete/<id>', views.delete )
]
