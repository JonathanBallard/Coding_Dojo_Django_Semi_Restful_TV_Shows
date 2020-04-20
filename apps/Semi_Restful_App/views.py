from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
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

    errors = Show.objects.validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request,v)
        return redirect('/shows/new/')
    else:
        Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc = request.POST['description'])
        messages.success(request,"Show created successfully!")
    return redirect('/shows/')

def thisShow(request, id):
    context = {
        "show" : Show.objects.get(id=id),
    }
    return render(request, 'Semi_Restful_App/this_show.html',context)

def editThisShow(request,id):
    context = {
        "show" : Show.objects.get(id=id),
    }
    return render(request, 'Semi_Restful_App/edit_show.html', context)

def updateThisShow(request,id):

    errors = Show.objects.validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request,v)
        return redirect('/shows/' + id + '/edit/')
    else:
        updateShow = Show.objects.get(id=id)
        updateShow.title=request.POST['title']
        updateShow.network=request.POST['network']
        updateShow.release_date=request.POST['release_date']
        updateShow.desc = request.POST['description']
        updateShow.save()
        messages.success(request,"Show updated successfully!")
    return redirect('/shows/')




    return redirect('/shows/')

def destroyThisShow(request,id):
    delShow = Show.objects.get(id=id)
    delShow.delete()
    return redirect('/shows/')













