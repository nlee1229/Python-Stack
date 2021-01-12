from django.urls import path 
from . import views # . signifies on the same level of folders

urlpatterns = [
    path('', views.root), #index is the method that we're referencing to
    path('blogs', views.index), #making a route to blogs
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:number>', views.show),
    path('blogs/<int:number>/edit', views.edit),
    path('blogs/<int:number>/delete', views.destroy),
    path('blogs/json', views.jason),
] 