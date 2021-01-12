from django.shortcuts import redirect, render, HttpResponse
from .models import Ninja, Dojo


def index(request):
	context = {
		"dojos": Dojo.objects.all(),
		"ninjas": Ninja.objects.all()
	}
	return render(request, 'index.html', context)


def dojo_add(request):

    dojo_name = request.POST.get('name')
    dojo_city = request.POST.get('city')
    dojo_state = request.POST.get('state')
    Dojo.objects.create(name=dojo_name, city=dojo_city, state=dojo_state)
    return redirect('/')


def ninja_add(request):

    dojo = Dojo.objects.get(id=request.POST.get('dojo_id'))
    fname = request.POST.get('fName')
    lname = request.POST.get('lName')
    Ninja.objects.create(first_name=fname, last_name=lname, dojo=dojo)
    return redirect('/')


def delete_info(request):
	d = Dojo.objects.get(id=request.POST.get('deletor'))
	d.delete()
	return redirect('/')