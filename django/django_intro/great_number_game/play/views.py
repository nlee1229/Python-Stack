from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):
    if 'random_num' not in request.session:
        request.session['random_num'] = random.randint(1,100)
    
    if 'display_low' not in request.session:
        request.session['display_low'] = ""
    
    if 'display_high' not in request.session:
        request.session['display_high'] = ""
    
    if 'answer' not in request.session: 
        request.session['answer'] = ""

    print(request.session['random_num'])
    return render(request, 'index.html')

def guess(request):
    num_guess = int(request.POST['number'])

    if num_guess < request.session['random_num']:
        request.session['display_low'] = "show_low"
        print("TOO LOW")
        if request.session['display_high'] == request.session['display_high']: 
            del request.session['display_high']

    elif num_guess == request.session['random_num']:
        if request.session['display_high'] == request.session['display_high'] or request.session['display_low'] == request.session['display_low']:
            del request.session['display_high']
            del request.session['display_low']
        request.session['answer'] = "correct"
        print("YOU GOT IT")

    elif num_guess > request.session['random_num']:
        request.session['display_high'] = "show_high"
        print("TOO HIGH")
        if request.session['display_low'] == request.session['display_low']:
            del request.session['display_low']

    return redirect('/')

def reset(request):
    del request.session['random_num']
    del request.session['display_low']
    del request.session['display_high']
    del request.session['answer']
    return redirect('/')





    




