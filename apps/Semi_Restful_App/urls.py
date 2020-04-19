from django.urls import path 
from . import views 
 
urlpatterns = [ 
    path('', views.index), 
    path('shows/', views.shows), 
    path('shows/new/', views.newShow), 
    path('shows/create/', views.createShow), 
    path('shows/<int:id>/', views.thisShow), 
    path('shows/<int:id>/edit/', views.editThisShow), 
    path('shows/<int:id>/update/', views.updateThisShow), 
    path('shows/<int:id>/destroy/', views.destroyThisShow), 
 
] 
 
 
