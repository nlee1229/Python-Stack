from django.shortcuts import render, redirect, HttpResponse
from .models import User

def index(request):
    context={
        "allusers" : User.objects.all()
    }
    return render(request, "index.html", context)

def data(request): 
    data = User()

    data.first_name = request.POST.get('first_name')
    data.last_name = request.POST.get('last_name')
    data.email = request.POST.get('email')
    data.age = request.POST.get('age')

    data.save()

    return redirect('/')



