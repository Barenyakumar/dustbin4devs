from django.contrib import admin
from django.urls import path, include
from . import views
 
urlpatterns = [
    path('',views.home,name='home'),
    path('pastetext',views.pastetext,name='pastetext'),
    path('showtext/<str:pk>',views.showtext,name='showtext'),
    path('deletetext/<str:pk>',views.deletetext,name='deletetext'),
    path('renewexpiry/<str:pk>',views.renewexpiry,name='renewexpiry'),
    path('login',views.loginUser,name='loginUser'),
    path('register',views.registerUser,name='registerUser'),
    path('logout',views.logoutUser,name='logoutUser'),

]
