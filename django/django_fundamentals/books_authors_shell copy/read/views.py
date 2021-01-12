from django.shortcuts import redirect, render, HttpResponse
from .models import Book, Author

def index(request):
    context = {
        "allbooks": Book.objects.all(),
        "allauthors": Author.objects.all(),
    }
    return render(request, 'index.html', context)

def addbook(request):
    book_title = request.POST.get('title')
    book_descrip = request.POST.get('description')
    Book.objects.create(title = book_title, desc = book_descrip)
    return redirect('/')

def book_info(request, id):
    context = {
        "bookid": Book.objects.get(id=id),
        "allauthors2": Author.objects.all(),
    }
    return render(request, 'index2.html', context)

def author_adding(request):
    this_author = Author.objects.get(id=request.POST["authorid"]) 
    this_book = Book.objects.get(id=request.POST["bookyid"])
    
    this_book.authors.add(this_author)
    return redirect(f"/viewbook/{this_book.id}")

def author_info(request):
    context = {
        "allauthors3": Author.objects.all(),
        "book3": Book.objects.all(),
    }
    return render(request, 'index3.html', context)

def add_an_author(request):
    author_fname = request.POST.get('first_name')
    author_lname = request.POST.get('last_name')
    author_notes = request.POST.get('notes')

    Author.objects.create(first_name = author_fname, last_name = author_lname, notes = author_notes)
    return redirect('/author')


def author_page(request,id):
    context = {
        "an_author": Author.objects.get(id=id),
        "more_books": Book.objects.all(), 
    }
    return render(request, 'index4.html', context)


def book_adding(request):
    this_booker = Book.objects.get(id=request.POST["more_books"]) 
    this_authory = Author.objects.get(id=request.POST["authoryid"])

    this_authory.books.add(this_booker)
    return redirect(f"/viewauthor/{this_authory.id}")







