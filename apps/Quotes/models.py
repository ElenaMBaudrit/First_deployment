# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from datetime import date
import bcrypt, datetime
import re 

# Create your models here.
class UserManager(models.Manager):
    def valid_reg(self, postData):
        print postData 
        errors = []
        name = postData['name']
        alias = postData['alias']
        email = postData['email']
        password = postData['password']
        c_password = postData['c_password']
        birthday = postData['birthday']

        if len(name) is 0:
            errors.append('Name is required')
        elif len(name) < 3:
            errors.append('Name must be at least 3 characters')
        if len(alias) is 0:
            errors.append('Alias is required')
        elif len(alias) < 3:
            errors.append('Alias must be at least 3 characters')
        if len(email) is 0:
            errors.append('Email is required')

        if len(password) is 0:
            errors.append('Password is required')
        elif len(password) < 8:
            errors.append('Password must be at least 8 characters')
        elif password != c_password:
            errors.append('Passwords must match')
        if len(birthday) is 0:
            errors.append('Date of Birth is required')

        if len(errors) > 0:
            return (False, errors)
        else:
            result = self.filter(name=name)
            if len(result) > 0:
                errors.append('User Name already exists')
                return (False, errors)
            else:
                new_user = self.create(
                    name = name,
                    password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                )
                return (True, new_user)

        if len(errors) > 0:
            return (False, errors)
        else:
            result = self.filter(email=email)
            if len(result) > 0:
                # email exists
                errors.append('Email already exists')
                return (False, errors)
            else:
                new_user = self.create(
                    name =name,
                    email = email,
                    password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()),
                    birthday = birthday
                )
                return (True, new_user)

    def validate_log(self, postData):
        errors = []
        print postData
        password = postData['password']
        email = postData['email']
        if len(password) is 0:
            errors.append('Password is required')
        if len(email) is 0:
            errors.append('Email is required')

        if len(errors) > 0:
            return (False, errors)
        else:
            result = self.filter(quote=quote)
            if len(result) > 0:
                errors.append('Provide the requested information')
                return (False, errors)
            else:
                new_quote= self.create(
                    author = author,
                    description = description
                    
                )
                return (True, new_quote)

        if len(errors) > 0:
            return (False, errors)
        else:
            result = self.filter(email=email)
            if len(result) > 0:
                # email exists
                errors.append('Email already exists')
                return (False, errors)
            else:
                new_user = self.create(
                    name =name,
                    email = email,
                    password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()),
                    birthday = birthday
                )
                return (True, new_user)


class QuoteManager(models.Manager):
    def validate_quote(self, postData):
        print postData['author']
        errors = []
        author = postData['author']
        description = postData['description']

        if len(author) is 0:
            errors.append('Author is required')
        elif len(author) < 3:
            errors.append('Author must be at least 3 characters')
        if len(description) is 0:
            errors.append('Quote is required')
        elif len(description) < 10:
            errors.append('Quote must be have at lease 10 characters')
        if len(errors) > 0:
            return (False, errors)
        else: 
            result = self.filter(quote = quote)
            if len(result) is 0:
                new_user = self.create(
                    name =name,
                    email = email,
                    password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()),
                    birthday = birthday
                )
                return (True, new_quote)

class User(models.Model):
    name = models.CharField (max_length = 255)
    alias = models.CharField (max_length = 255)
    email = models.EmailField(max_length = 254)
    password = models.CharField (max_length = 255)
    birthday = models.DateField (null=True, blank=True)
    objects = UserManager()    

    created_at = models.DateTimeField (auto_now_add = True)
    updated_at = models.DateTimeField (auto_now = True)

    def __str__(self):
        return self.name

class Quote(models.Model):
    author = models.CharField (max_length = 255)
    description = models.TextField (max_length = 1000)
    creator = models.ForeignKey (User, related_name = "added_by")
    others = models.ManyToManyField (User, related_name = "others_quotes")
    objects = QuoteManager()

    created_at = models.DateTimeField (auto_now_add = True)
    updated_at = models.DateTimeField (auto_now = True)

    def __str__(self):
        return self.autor







