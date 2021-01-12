from django.shortcuts import render, redirect, HttpResponse


def index(request):
    if 'page_counter' in request.session: #request.session is the dictionary
        request.session['page_counter'] += 1 #second, this runs. if there is a key, this adds the 1 to the value of the key
    else:
        request.session['page_counter'] = 1 #first runs this line. Then this command tells it to create a key and start at 1
    print('page_counter')
    return render(request, 'index.html')

def destroy(request):
    del request.session['counter']
    return redirect('/')

def double_button(request): 
    if 'counter' in request.session:
        request.session['counter'] += 2
    else:
        request.session['counter'] = 1
    print('counter')
    return render(request, 'index.html')

def increment(request): 
    user_num = request.POST['number']
    if 'counter' in request.session:
        request.session['counter'] += int(user_num)
    else: 
        request.session['counter'] = int(user_num)
    print('counter')
    return render(request, 'index.html') 


# So request.session is the dictionary. Once you run the python manage.py migrate command, that is what creates the session dictionary.

# Once you’ve created the dictionary, then you can add key + value pairs whenever you want. 

