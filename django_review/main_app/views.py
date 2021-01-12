from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.


def home(request):
    context = {
        "dojo": Dojo.objects.all(),
        "ninja": Ninja.objects.all(),
    }
    return render(request, "home.html", context)


# Process the form page for adding dojo/ninja
def add(request):
    if request.POST['form'] == "Ninja":
        if request.POST
        dojoid = Dojo.objects.get(id=request.POST['dojo_select'])

        Ninja.objects.create(
            fname=request.POST['fname'],
            lname=request.POST['lname'],
            dojoid=dojoid,
        )

    if request.POST['form'] == "Dojo":
        Dojo.objects.create(
            name=request.POST['name'],
            city=request.POST['city'],
            state=request.POST['state'],
        )
    return redirect("/")

# Delete the dojos which also deletes the ninjas inside


def delete(request, id):
    d = Dojo.objects.get(id=id)
    d.delete()

    return redirect("/")
