from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

#Login index page. If user is logged in should redirect to dashboard
def index(request):
    try:
        request.session['logged_in']
        return redirect(reverse('login_wishboard', kwargs={'id':request.session['logged_in']}))
    except KeyError:
        return render(request, 'login/index.html')

#Routes to registration page where data is inputted
def register(request):
    try:
        request.session['logged_in']
        return redirect(reverse('login_wishboard', kwargs={'id':request.session['logged_in']}))
    except KeyError:
        return render(request, 'login/register.html')
#Processes data from registration tha user inputted in the form
def registration(request):
    results = User.objects.valid_registration(request.POST)
    if results[0]:
        return redirect('login_index')
    else:
        errors = results[1]
        for error in errors:
            messages.error(request, error)
        return redirect('login_register')

#Login the user
def login(request):
    results = User.objects.valid_login(request.POST)
    if results[0]:
        passFlag = True
        if 'logged_in' not in request.session:
            email = request.POST['email']
            request.session['logged_in'] = User.objects.get(email=email).id
            return redirect(reverse('login_wishboard', kwargs={'id':request.session['logged_in']}))
    else:
        passFlag = False
        errors = results[1]
        for error in errors:
            messages.error(request, error)
        return redirect(reverse('login_index'))

#Clear session and logout the user
def logout(request):
    request.session.clear()
    return redirect('login_index')
    




    
        
