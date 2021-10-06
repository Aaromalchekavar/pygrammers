from django.http import HttpResponse
from django.shortcuts import render, redirect


# detail = {}


# def details(req):

# name = req.POST['name']
# bloodgroup = req.POST['bloodgroup']
# age = req.POST['age']

# detail[name] = [bloodgroup, age]

# return render(req, 'details.html', {'details': detail})


def home(req):
    if req.session.has_key('username'):
        if req.session.has_key('password'):
    # username = req.POST['username']
    # password = req.POST['password']
    # for key,value in user.items:
    #     if key==username and value[1]==password:
            return render(req, 'index.html')
    # return render(req, 'usererror.html')
    return redirect('/login')

user = {}


def user_details(req):

    username = req.POST['username']
    first_name = req.POST['first_name']
    last_name = req.POST['last_name']
    password = req.POST['password']
    phone = req.POST['phone']

    user[username] = [first_name+' '+last_name, password, phone]

    return render(req, 'user_details.html', {'user': user})
