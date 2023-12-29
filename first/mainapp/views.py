from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import Guide 


# Create your views here.

def HomePage(request):
    
    return render(request, 'added.html')

def TouristPage(request):
    return render(request, 'Touristform.html')


def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def ProfileOne(request):
    return render(request, 'profile1.html')

def Goutput(request):
    my_data = Guide.objects.all() #for all the records 
    context={
       
      'my_data':my_data,
      
    
    } 

    return render(request, 'guideoutput.html',context)


def GuideDetails(request):
    if request.method=='POST':
        
        fname=request.POST.get('fname')
        Age=request.POST.get('Age')
        Contact=request.POST.get('Contact')
        gender=request.POST.get('gender')
        Address=request.POST.get('address')
        Price=request.POST.get('Price')
        Language=request.POST.get('Language')
        subject=request.POST.get('subject')
        x=Guide()
        x.firstname=fname
        x.age=Age
        x.contact=Contact
        x.gender=gender
        x.address=Address
        x.price=Price
        x.language=Language
        x.subject=subject
        x.save()
        return redirect('guidedetails')
    return render(request, 'guidedetails.html')


def Guideform(request):
    if request.method=='POST':
        username=request.POST.get('username')
        passw=request.POST.get('password')
        user=authenticate(request,username=username,password=passw)
        if user is not None:
            login(request,user)
            return redirect('guidedetails')
        else:
            return HttpResponse('Incorrect info')
    return render(request, 'Guideform.html')



def Signup(request):
    if request.method=='POST':
        uname=request.POST.get('userName')
        email=request.POST.get('email')
        pw=request.POST.get('password')
        my_user=User.objects.create_user(uname,email,pw)
        my_user.save()
        
        
        
        
    return render(request,'signUP.html')

def LoginPage(request):
    if request.method=='POST':
        uname2=request.POST.get('username')
        passw=request.POST.get('password')
        user=authenticate(request,username=uname2,password=passw)
        if user is not None:
            login(request,user)
            return redirect('guidedetails.html')
        else:
            return HttpResponse('Incorrect info')
    return render(request,'login.html')


# from openpyxl import Workbook

# def write_user_data_to_excel(my_user):
#     # Create a new workbook and add a worksheet
#     wb = Workbook()
#     ws = wb.active

#     # Write the headers to the worksheet
#     ws.append(['Username', 'Email' ])

#     # Write each user's data to the worksheet
#     for user in my_user:
#         ws.append([user.userName, user.email])

#     # Save the workbook
#     wb.save('user_data.xlsx')