from django.shortcuts import render, HttpResponse, redirect
from login_reg.models import User

def index(request):
	context = {
        "myuser" : User.objects.get(id = request.session['user_id'])
    }
	return render(request, 'index.html', context)