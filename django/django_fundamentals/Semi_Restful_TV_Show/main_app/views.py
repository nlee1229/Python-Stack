from django.shortcuts import redirect, render, HttpResponse
from .models import Show
from django.contrib import messages


#Redirects to homepage below------------------------>
def redirect_to_shows(request):
    return redirect('/shows')

#Below is for index.html--------------------------->
def index(request):
    context = {
        "shows": Show.objects.all(),
    }
    return render(request, 'index.html', context)

#Below is for index2.html--------------------------->

def add_show(request):
    context = {
        "shows2" : Show.objects.all(),
    }
    return render(request, 'index2.html')

def create_show(request):

    errors = Show.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')

    show_title = request.POST['title']
    show_network = request.POST['network']
    show_rel_date = request.POST['rel_date']
    show_descrip = request.POST['show_desc']
    new_show = Show.objects.create(
        title = show_title, 
        network = show_network, 
        release_date = show_rel_date, 
        desc = show_descrip
        )
    id = new_show.id
    return redirect(f'/shows/{id}')

    
#Below is for index3.html------------------->

def show_id_page(request, id):
    context = {
        "shows3" : Show.objects.get(id=id),
    }
    return render(request, 'index3.html', context)

#Below is for index4.html-------------------->

def edit_show(request, id):
    context = {
        "shows4" : Show.objects.get(id=id),
    }

    return render(request, 'index4.html', context)

def update_show(request, id): 

    show_update = Show.objects.get(id=id)

    errors = Show.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_update.id}/edit')


    show_update.title = request.POST.get('title')

    show_update.network = request.POST.get('network')

    show_update.release_date = request.POST.get('rel_date')

    show_update.desc = request.POST.get('show_desc')

    show_update.save()

    return redirect(f'/shows/{show_update.id}')

# Delete function for both main page and other page----

def delete_show(request, id):
    show_delete = Show.objects.get(id=id)
    show_delete.delete()

    return redirect('/shows')
