from django.http import HttpResponse
from django.shortcuts import render
from .models import Details


def home(req):
    return render(req, 'index.html', {'title': 'Login form'})

detail = {}

def details(req):

    name = req.POST['name']
    bloodgroup = req.POST['bloodgroup']
    age = req.POST['age']

    detail[name] = [bloodgroup,age]
    

    return render(req, 'details.html',{'details':detail})
