from django.urls import path 
from . import views

urlpatterns= [
    path('', views.redirect_to_shows),
    path('shows', views.index),
    path('shows/<int:id>', views.show_id_page),
    #Links below go to index.html
    path('shows/new', views.add_show),
    path('shows/create', views.create_show),
    path('shows/<int:id>/edit', views.edit_show),
    path('shows/<int:id>/update', views.update_show),
    path('shows/<int:id>/destroy',views.delete_show),
]