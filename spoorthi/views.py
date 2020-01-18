from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from .models import Register
from django.db.models import *


def home(request):
	return render(request,'spoorthi/home.html')

def events(request):
	return render(request,'spoorthi/events.html')

def contact(request):
	return render(request,'spoorthi/contact.html')

def gallery(request):
	return render(request,'spoorthi/gallery.html')

def new(request):
	return render(request,'spoorthi/new.html')
    
def sponsor(request):
    return render(request,'spoorthi/sponsors.html')

def register(request):
    # return render(request,'blog.html')
    if request.method == 'POST':
        # form = forms.NewsLetterSubscribe(request.POST)
        # if form.is_valid():
        inputEvent = request.POST.get('inputEvent')
        inputName = request.POST.get('inputName')
        inputEmail = request.POST.get('inputEmail')
        inputNumber = request.POST.get('inputNumber')
        inputCollege = request.POST.get('inputCollege')
        inputDescription = request.POST.get('inputDescription')
        form = Register()
        form.event = inputEvent
        form.full_name = inputName
        form.email = inputEmail
        form.number = inputNumber
        form.college = inputCollege
        form.description = inputDescription
        form.save()
        print(form.full_name)
        subject="Successfully Registered For SPoorthi 2020" 
        message ="Greetings,\nHello "+ form.full_name +", you have succesfully registered for " + form.event+".\n Please Show this email at the time of Event."+"\nSee you at SPoorthi 2020 from 13th-31st January 2020.\n\n"+"Registration Fees can be paid on:"+"\n"+"1)GPay: 7715018288"+"\n"+"2)Paytm: 9821675495\n"+"\n\n"+"Details You Filled In"+"\n\n"+"Event Name: "+form.event+"\n"+"Full Name: "+form.full_name+"\n"+"Email: "+form.email+"\nNumber: "+form.number+"\n"+"College: "+form.college+"\n"+"Description: "+form.description+"\n\n"+"Thanks and Regards,"+"\n"+"SPoorthi SPIT\n"
        from_email=settings.EMAIL_HOST_USER
        to_list=[form.email]
        print(form.email)
        val=send_mail(subject,message,from_email,to_list,fail_silently=False)
        print(val)
        return redirect('register')
    # else:
    # 	form = Register()
    return render(request,'spoorthi/register.html')