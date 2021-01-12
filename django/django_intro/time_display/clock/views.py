from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
    gshock = {
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%H: %M %p", gmtime()),
        
    }
    return render(request,'index.html', gshock)