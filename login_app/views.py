from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "GET":
        return redirect('/')

    errors = User.objects.basic_validator(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect("/")
    else:
        user = User.objects.register(request.POST)
        request.session['userid'] = user.id
        return redirect("/quotes/")

def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['pw']):
        messages.error(request, "Invalid email/password")
        return redirect("/")
    user = User.objects.get(email = request.POST['email'])
    request.session['userid'] = user.id
    return redirect("/quotes/")

def logout(request):
    request.session.clear()
    return redirect("/")

