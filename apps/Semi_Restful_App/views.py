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
    return render(request, 'Semi_Restful_App/new_show.html')

def createShow(request):
    Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc = request.POST['description'])

    return redirect('/shows/')

def thisShow(request, id):
    context = {
        "this_show" : Show.objects.get(id=id),
    }
    return render(request, 'Semi_Restful_App/this_show.html',context)

def editThisShow(request,id):
    context = {
        "this_show" : Show.objects.get(id=id),
    }
    return render(request, 'Semi_Restful_App/edit_show.html', context)

def updateThisShow(request,id):

    updateShow = Show.objects.get(id=id)
    updateShow.title=request.POST['title']
    updateShow.network=request.POST['network']
    updateShow.release_date=request.POST['release_date']
    updateShow.desc = request.POST['description']

    updateShow.save()

    return redirect('/shows/')

def destroyThisShow(request,id):
    delShow = Show.objects.get(id=id)
    delShow.delete()
    return redirect('/shows/')













