from __future__ import unicode_literals
from ..login.models import User
from django.contrib import messages
from django.db import models


#This mainly checks for blank field when user inputs item
class ManageItems(models.Manager):
    def validate_items(self, post_data, request):
        passFlag = True
        if len(post_data['item_desired']) < 2:
            messages.warning(request, "Item must be at leas 3 characters")
            passFlag = false

        #LOGIN
        if passFlag:
            logged_in = request.session['logged_in']
            user_item = User.objects.get(id=logged_in)
            make_item = User.objects.get(id=logged_in)
            item = self.create(description = post_data['item_desired'], item_id = user_item)
        return passFlag

class Item(models.Model):
    description = models.TextField(max_length=100)
    item_id = models.ForeignKey(User, related_name="user_item")
    make_item_id = models.ManyToManyField(User, related_name="make_item")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ManageItems()
    

















