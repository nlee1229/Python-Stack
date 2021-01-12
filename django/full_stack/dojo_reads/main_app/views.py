from django.shortcuts import render, HttpResponse, redirect
from login_reg.models import User
from .models import *

def index(request):
    context = {
        "user" : User.objects.get(id = request.session['user_id'])
    }
    return render(request, "books.html", context)

def addbook(request):
    return render(request, "booksadd.html")

def procbook(request):
    newbook = Book.objects.create(
        title = request.POST['title']
    )
    id = newbook.id
    
    Review.objects.create(
        review = request.POST['review'],
        rating = request.POST['rating'],
        forbook = Book.objects.get(id = id),
        byuser = User.objects.get(id = request.session['user_id']),
    )
    
    newauthor = Author.objects.create(
        name = request.POST['newauthor']
    )
    
    newbook.authors.add(newauthor)
    
    return redirect(f"/books/{id}")


def bookinfo(request, id):
    context = {
        "book": Book.objects.get(id = id)
    }
    return render(request, "booksinfo.html", context)