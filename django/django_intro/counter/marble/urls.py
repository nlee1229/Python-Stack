from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index),
    path('destroy', views.destroy),
    path('double', views.double_button),
    path('increment', views.increment),
    
]  