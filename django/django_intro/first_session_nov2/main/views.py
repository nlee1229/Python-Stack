from django.shortcuts import render, redirect, HttpResponse

def index(request):
    request.session['name'] = "George" #how we access our session dictionary
    return render(request, "index.html")

def process(request):
    name = request.POST['name']


    request.session['name_submitted'] = name
    return redirect(f'/{name}')

def say_hi(request, name):
    return HttpResponse(f"{name} says hi!")

