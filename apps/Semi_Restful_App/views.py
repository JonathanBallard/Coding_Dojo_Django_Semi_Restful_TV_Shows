from django.shortcuts import render, redirect 
from .models import * 
 
 
 
# Create your views here. 
def index(request): 
    return redirect('shows/')

def shows(request):
    context = {
        "all_shows" : Show.objects.all()
    }
    return render(request, 'Semi_Restful_App/index.html', context) 

def newShow(request):
    return render(request, 'Semi_Restful_app/new_show.html')

def createShow(request):
    Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc = request.POST['description'])

    return redirect('shows/')

def thisShow(request, id):
    pass

def editThisShow(request,id):
    pass

def updateThisShow(request,id):
    pass

def destroyThisShow(request,id):
    pass













