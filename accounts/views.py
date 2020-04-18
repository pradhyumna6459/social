from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import data
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("afterlogin")
        else:
            messages.info(request,'invalid user')
            return redirect('login')


    else:
        return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email=request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name,
                                                last_name=last_name,email=email)
                user.save();
                return redirect('login')
        else:
            print("password not matching")
            return redirect('signup')


    else:
        return render(request,'RegisterPage.html')

# Create your views here.
def Register(request):
    return render(request,'RegisterPage.html')
def home(request):
    return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')

def afterlogin(request):
    datas=data.objects.all()

    return render(request,'afterlogin.html',{'datas':datas})

def contact(request):
    return render(request,'contact.html')

def meetTheTeam(request):
    return render(request,'meetTheTeam.html')

def ngo(request):
    return render(request,'ngo.html')