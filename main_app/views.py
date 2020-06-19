from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import Profile, City, Post



# Create your views here.
def home(request):
    form = SignUpForm() 
    context = {'form': form}
    return render(request,'home.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("worked")
            name = form.cleaned_data ['name']
            current_city = form.cleaned_data ['current_city']
            user = form.save()
            Profile.objects.create(user=user, name=name, current_city=current_city)
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
    profile = Profile.objects.get(user = request.user)
    posts = Post.objects.filter(author=request.user)
    if request.method == 'POST':
        user.name = request.POST['name']
        user.current_city = request.POST['current_city']
        user.save()
        return redirect('profile')
    else:
        context = {'profile': profile, 'posts': posts}
        return render(request, 'profile.html', context)

def show_post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'profile/show_post.html', context)
    