from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'index.html')

def index2(request):
    user_name = request.POST["user_name"]
    user_location = request.POST["location"]
    user_languages = request.POST["languages"]
    user_textarea = request.POST["comment_box"]

    context = {
        "name": user_name, 
        "location": user_location,
        "languages": user_languages,
        "text": user_textarea,
    }
    return render(request, 'index2.html', context)

def goback(request): 
    return redirect('/')

