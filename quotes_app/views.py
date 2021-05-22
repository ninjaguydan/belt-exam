from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def dashboard(request):
    if "userid" not in request.session:
        return redirect("/")
    context = {
        "user" : User.objects.get(id = request.session['userid']),
        "quotes" : Quote.objects.all(),
    }
    return render(request, "dashboard.html", context)

def add_quote(request):
    if request.method == "GET":
        return redirect('/quotes/')
    errors = Quote.objects.validator(request.POST)
    if errors:
        for error in errors.values():
            messages.error(request, error)
        return redirect ('/quotes/')
    user = User.objects.get(id = request.session['userid'])
    Quote.objects.create(
        author = request.POST['author'],
        content = request.POST['quote'],
        added_by = user
    )
    return redirect ('/quotes/')

def delete_quote(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    quote.delete()
    return redirect('/quotes/')

def profile(request, profile_id):
    return render(request, "profile.html", {"profile": User.objects.get(id=profile_id)})

def edit(request):
    return render(request, "edit.html", {"user" : User.objects.get(id=request.session['userid'])})

def update_account(request):
    if request.method == "GET":
        return redirect('/quotes/')
    errors = User.objects.update(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect("/quotes/myaccount")
    user = User.objects.get(id=request.session['userid'])
    user.first_name = request.POST['fname']
    user.last_name = request.POST['lname']
    user.email = request.POST['email']
    user.save()
    return redirect(f'/quotes/user/{user.id}')

def like(request, quote_id):
    user = User.objects.get(id=request.session['userid'])
    quote = Quote.objects.get(id=quote_id)
    quote.likes.add(user)
    return redirect('/quotes/')
    
def unlike(request, quote_id):
    user = User.objects.get(id=request.session['userid'])
    quote = Quote.objects.get(id=quote_id)
    quote.likes.remove(user)
    return redirect('/quotes/')