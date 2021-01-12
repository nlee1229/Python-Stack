from django.db import models
from login_reg.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Author(models.Model):
    name = models.CharField(max_length = 255)
    author = models.ManyToManyField(Book, related_name = "authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Review(models.Model):
    review = models.CharField(max_length=255)
    rating = models.IntegerField(blank=True, null=True)
    forbook = models.ForeignKey(Book, related_name="forbooks", on_delete= models.CASCADE)
    byuser = models.ForeignKey(User, related_name="byusers", on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)