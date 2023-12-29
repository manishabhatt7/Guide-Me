from django.contrib import admin
from django.urls import path,include
from mainapp import views

urlpatterns = [
    path('',views.HomePage,name='home'),
    path('tourist',views.TouristPage,name='tourist'),
    path('signup',views.Signup,name='signup'),
    path('guidedetails',views.GuideDetails,name='guidedetails'),
    path('Guideform',views.Guideform,name='Guideform'),
    path('profile1',views.ProfileOne,name='profile1'),
    path('guideoutput',views.Goutput,name='guideoutput'),
    path('about',views.About,name='about'),
    path('contact',views.Contact,name='contact')
]
