from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

from .models import Profile


# Create your views here.
def home(request):
    form = SignUpForm() 
    context = {'form': form}
    return render(request,'home.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            current_city = form.cleaned_data ['current_city']
            user = form.save()
            Profile.objects.create (user=user.pk, name=name, current_city=current_city)
            login(request,user)
            return redirect('profile')
    else:
        form = SignUpForm() 
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
    user = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        user.name = request.POST['name']
        user.current_city = request.POST['current_city']
        user.save()
        return redirect('profile')
    else:
        context = {'user': user}
        return render(request, 'profile.html', context)
    
    