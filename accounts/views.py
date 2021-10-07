from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.http import JsonResponse
#for back button clear cache
from django.views.decorators.cache import cache_control
# Create your views here.
from django.core.cache import cache
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def default(req):
    return redirect('/login')


def signup(req):
    if req.session.has_key('username'):
        username = req.session['username']
        if req.session.has_key('password'):
            password = req.session['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                return redirect('/display')
    elif req.method == 'POST':
        username = req.POST['username']
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        password1 = req.POST['password1']
        password2 = req.POST['password2']
        email = req.POST['email']
        if User.objects.filter(username=username).exists():
            messages.info(req, 'username already taken')
            return redirect('/signup')
        if password1 == password2:
            user = User.objects.create_user(
                username=username, last_name=last_name, first_name=first_name, password=password1, email=email)
            user.save()
            return redirect('/login')
        else:
            messages.info(req, 'mismatching passwords')

    return render(req, 'signup.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(req):
    if req.session.has_key('username'):
        username = req.session['username']
        if req.session.has_key('password'):
            password = req.session['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                return redirect('/display')
    elif req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        print(username, password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # auth.login(req, user)
            req.session['username'] = username
            req.session['password'] = password
            return JsonResponse(
                {'success':True},
                safe=False
            )
        else:
            auth.login
            return JsonResponse(
                {'success':False},
                safe=False
            )
    return render(req, 'login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(req):
    if req.session.has_key('username'):
        if req.session.has_key('password'):
            try:
                # req.session.clear()
                # cache.clear()
                req.session.flush()
                req.session.modified = True
                # response = redirect('/login')
                # response.delete_cookie('sessionid')
                # return response
            except:
                print('unable to delete session')
                pass
    return redirect('/')

