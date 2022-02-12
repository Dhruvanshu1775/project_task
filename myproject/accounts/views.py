from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user_obj = User.objects.filter(username = username)
        if user_obj :
            user = auth.authenticate(username = username, password = password)
            if user:
                auth.login(request,user)
                return redirect('dashboard')
            else:
                context = {
                    'password':'Enter corrent password',
                    'username':username,
                }
                return render(request, 'login.html', context)    

        else:
            context = {
                'login':'No User Found',
                'username':username,

            }
            return render(request, 'login.html', context)    

        user = auth.authenticate(username = username, password = password)
        if user:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            return redirect('login')    
    return render(request, "login.html")


def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = make_password(request.POST['password'])

        User.objects.create(username = username, email = email, password = password)
        return redirect('login')

    return render(request, "login.html")

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('login')


def dashboard(request):
	return render(request, 'dashboard.html')



