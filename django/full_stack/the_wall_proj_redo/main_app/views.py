from django.shortcuts import redirect, render
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    print(User.objects.all())
    return render(request, 'index.html')

#?????????????????????????????
def register(request):
    errs = User.objects.register_validator(request.POST)
    if len(errs) > 0:
        for msg in errs.values():
            messages.error(request, msg) #built-in function
        return redirect('/') #messages is being displayed in index.html
    password = request.POST['password']
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    print(password)
    print(hashed)

    new_user = User.objects.create(
        fname=request.POST['fname'],
        lname=request.POST['lname'],
        email=request.POST['email'],
        password=hashed,
    )
    request.session['user_id'] = new_user.id
    return redirect('/success')

def login(request):

    #checking if the email is in the database
    #using filter b/c filter goes into find all of the user objects in the email=request.POST['email'] query & put em in a list and give you the list back. CANNOT USE GET! For example, if there are 2 diff people that register using the same email, the GET function will cause an ERROR . GET only gives one user.
    user_list=User.objects.filter(email=request.POST['email'])
    if user_list: #checks if the list is empty or not. Sees if there is anything in that data structure
        our_user = user_list[0]
        print(request.POST['password'])
        print(our_user.password)
        if bcrypt.checkpw(request.POST['password'].encode(),our_user.password.encode()):
            print("Passwords match!!") #does the password 
            request.session['user_id'] = our_user.id
            return redirect('/success')

        else:
            messages.error(request, "User not found, or passwords don't match!")
        return redirect('/')
#Function that shows which specific user has logged in
def success(request):
    logged_in_user = User.objects.get(id=request.session['user_id'])
    context={
        'logged_in_user': logged_in_user
    }
    return render(request, 'success.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

