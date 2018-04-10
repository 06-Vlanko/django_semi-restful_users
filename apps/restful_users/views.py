# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from .models import *

# Create your views here.
def sendToDefault(request):
    return redirect ('/users/')

def index (request):
    users = { 
        'users': User.objects.all()
        }
    return render (request, 'restful_users/index.html', users)

def new(request):
    return render (request, 'restful_users/new.html')

def create(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    print User.objects.get(id=1)
    return redirect ('/users/')

def show(request, user_id):
    context = {
        'user' : User.objects.get(id=user_id)
    }
    print context
    return render (request, 'restful_users/show.html', context)

def edit(request, user_id):
    context = {
        'user' : User.objects.get(id=user_id)
    }
    return render (request, 'restful_users/edit.html', context)

def update (request):
    user = User.objects.get(id=request.POST['user_id'])
    print '----> BEFORE CHANGES: ', user
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']

    user.save()

    print '----> AFTER CHANGES: ', user

    return redirect ('/users/'+request.POST['user_id'])

def destroy (request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect ('/users/')
