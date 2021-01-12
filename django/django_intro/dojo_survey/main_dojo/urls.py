from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('result',views.index2), #where did the result come from?
    path('goback', views.goback),
]