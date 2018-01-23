from django.shortcuts import render, redirect
from ..login.models import User
from .models import Item
from django.db import models
from django.http import HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse

#FOR DISPLAYING ITEMS ON THE INDEX PAGE WITH YOUR USER SPECIFIC INFO AND OTHERS
def wishlist(request, id):
    user = User.objects.get(id=request.session['logged_in'])
    context = {
        "loggedin": User.objects.get(id=id),
        "items": Item.objects.all(),
        "all_items": Item.objects.exclude(item_id=user).exclude(make_item_id=user.id),
    }
    return render(request, 'wishboard/index.html', context)


#LOADS THE CREATE ITEM PAGE
def item(request):
    return render(request, 'wishboard/create.html')

#VALIDATES THE INFORMATION URL NEEDS RENAMING
def create_item(request):
    if Item.objects.validate_items(request.POST, request):
        passFlag = True
        return redirect(reverse('login_wishboard', kwargs={'id':request.session['logged_in']}))
    else:
        passFlag = False
        return redirect(reverse('create_wish'))

#SHOW A SPECIFIC ITEM ON USERS WISHLIST
def show(request, id):
	context = {
		"items": Item.objects.get(id=id),
	}
	return render(request, 'wishboard/show.html', context)

#PUTS THE WISHLISTED ITEM IN YOUR OWN LIST
def join(request):
    if request.method == 'POST':
        grabber_id = request.POST['user']
        wanted_item_id = request.POST['item']
        grabber = User.objects.get(id=grabber_id)
        grab_item = Item.objects.get(id=wanted_item_id)
        grab_item.make_item_id.add(grabber)
        grab_item.save()
        return redirect(reverse('login_wishboard', kwargs={'id': request.session['logged_in']}))

#REMOVE SAID FAVORITED ITEM FROM YOUR PERSONAL LIST
def unjoin(request):
    if request.method == 'POST':
        remover_id = request.POST['user']
        wanted_remove_id = request.POST['item']
        remover = User.objects.get(id=remover_id)
        remove_item = Item.objects.get(id=wanted_remove_id)
        remove_item.make_item_id.remove(remover)
        remove_item.save()
        return redirect(reverse('login_wishboard', kwargs={'id': request.session['logged_in']}))
                
#REMOVES ITEM FROM YOUR PERSONAL LIST ONLY. 
def remove(request, id):
    Item.objects.get(id=id).delete()
    return redirect(reverse('login_wishboard', kwargs={'id': request.session['logged_in']}))








    
    
