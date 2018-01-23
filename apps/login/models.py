from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
from datetime import date, datetime
from dateutil.parser import parse as parse_date
import bcrypt, re, datetime

#UNICODE DATA
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = (r'^[A-Za-z]\w+$')

class UserManager(models.Manager):
    #VALIDATES LOGIN INFO CHECKING FOR PROPER FORMATTING
    def valid_registration(self, post_data):
        passFlag = True
        errors = []
        if len(post_data['name'] and post_data['username']) < 2:
            errors.append('Name needs and username to be 3 characters at least')
            passFlag = False
        if not re.match(NAME_REGEX, post_data['name']):
            errors.append('Name cannot contain letters/sybols')
            passFlag = False
        if not re.match(EMAIL_REGEX, post_data['email']):
            errors.append('INVALID EMAIL FORMAT')
            passFlag = False
        if len(post_data['password']) < 6:
            errors.append('Password gotta be 6 characters')
            passFlag = False
        if len(self.filter(email=post_data['email'])) > 0:
            errors.append('Registration invalid email in use already')
            passFlag = False
        if post_data['password'] != post_data['pw_confirm']:
            errors.append('Passwords gotta match!')
            passFlag = False


        #CHECK DATES FOR NOT BEING IN THE FUTURE
        unicode_text_start = post_data['date_hired']
        start_date = parse_date(unicode_text_start)
        if start_date.date() > date.today():
            errors.append("Start date cannot be in the future!")
            passFlag = False


        #HASH USER PASSWORD IF ALL FIELDS ARE CORRECT
        if passFlag == True:
            hashed = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())
            self.create(name = post_data['name'], date_hired = post_data['date_hired'], username = post_data['username'], email = post_data['email'], password = hashed)

        return [passFlag, errors]

    #VALIDATES INFO FOR LOGIN
    def valid_login(self, post_data):
        passFlag = True
        errors = []
        if len(User.objects.filter(email=post_data['email'])) > 0:
            hashed = User.objects.get(email = post_data['email']).password
            hashed = hashed.encode('utf-8')
            password = post_data['password']
            password = password.encode('utf-8')
            if bcrypt.hashpw(password, hashed) == hashed:
                passFlag = True
            else:
                errors.append("Unsuccessful Login")
                passFlag = False
        else:
            errors.append("Unsuccessful Login")
            passFlag = False
        return [passFlag, errors]

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)    
    date_hired = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()






















        










        
    
