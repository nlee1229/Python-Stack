from django.shortcuts import render, HttpResponse, redirect
from login_reg.models import User
from .models import *
from django.contrib import messages

def index(request):
    context = {
        "myuser" : User.objects.get(id = request.session['user_id']),

    }
    return render(request, 'dashboard.html', context)

def newtrip(request):
    
    return render(request, "new_trip.html")

def addtrip(request):

    errors = Trip.objects.validator(request.POST)

    if errors: 
        for value in errors.values():
            messages.error(request, value)
        return redirect('/main/books/newtrip')

    Trip.objects.create(
        destination = request.POST['destination'],
        start_date = request.POST['start_date'],
        end_date = request.POST['end_date'],
        content = request.POST['content'],
        by_user = User.objects.get(id=request.session['user_id']),
    )
    return redirect('/main/books')

def remove(request, id):
    trip_delete = Trip.objects.get(id=id)
    trip_delete.delete()

    return redirect('/main/books')

def edit(request, id):
    context = {
        "trips2": Trip.objects.get(id=id),
    }
    return render(request, 'edit_trip.html', context)

def update(request, id):

    trip_update = Trip.objects.get(id=id)

    errors = Trip.objects.validator(request.POST)

    if errors: 
        for value in errors.values():
            messages.error(request, value)
        return redirect(f'/main/books/{trip_update.id}/edit')

    trip_update.destination = request.POST.get('destination')
    trip_update.start_date = request.POST.get('start_date')
    trip_update.end_date = request.POST.get('end_date')
    trip_update.content = request.POST.get('content')

    trip_update.save()

    return redirect('/main/books')

def view(request, id):
    context = {
        "trips2": Trip.objects.get(id=id),
    }
    return render(request, 'view_trip.html', context)


    




