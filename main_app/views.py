from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    form = UserCreationForm() 
    context = {'form': form}
    return render(request,'home.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('profile')
    else:
        form = UserCreationForm() 
    context = {'form': form}
    return render(request,'home.html',context)

def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('profile')
    else:
        return HttpResponse("Error")

def user_logout(request):
    logout(request)
    return redirect('home')

def profile(request):
    return render(request, 'profile.html')