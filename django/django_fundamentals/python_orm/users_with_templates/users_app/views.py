from django.shortcuts import render, HttpResponse, redirect
from .models import Users


def index(request):
    context = {
		"allusers": Users.objects.all()
    }
    return render(request, "index.html", context)

def data(request):
	data = Users()
	#access data firstname		#what users typed in
	data.first_name = request.POST.get('first_name')
	data.last_name = request.POST.get('last_name')
	data.email = request.POST.get('email')
	data.age = request.POST.get('age')

	data.save()

	return redirect('/')


def delete(request):
	d = Users.objects.last()
	d.delete()
	return redirect('/')