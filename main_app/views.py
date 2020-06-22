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
        return redirect(f'/cities/8/')
    else:
        return HttpResponse("Error")

def user_logout(request):
    logout(request)
    return redirect('home')

def profile(request):
    profile = Profile.objects.get(user = request.user)
    posts = Post.objects.filter(author=request.user)
    if request.method == 'POST':
        profile.name = request.POST['name']
        profile.current_city = request.POST['current_city']
        profile.save()
        return redirect('profile')
    else:
        cities = City.objects.all()
        context = {'profile': profile, 'posts': posts,'cities':cities}
        return render(request, 'profile.html', context)

def cities(request):
    cities = City.objects.all()
    context = {'cities':cities}
    return render(request,'cities.html',context)

def show_city(request,city_id):
    cities = City.objects.all()
    city = City.objects.get(id=city_id)
    posts = Post.objects.filter(city=city_id).order_by('-date')
    context = {'city':city, 'posts':posts,'cities':cities}
    return render(request,'cities.html',context)

def show_post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'profile/show_post.html', context)
    

def add_post(request,city_id):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        city = City.objects.get(pk=city_id) 
        author = request.user
        post = Post.objects.create(title=title,content=content,city=city,author=author)
        post.save()
        return redirect('show_city', city_id=city.id)
    else:
        city = City.objects.get(id=city_id)
        context = {'city': city}
        return render(request,'add_post.html', context)

def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.save()
    return redirect('show_post', post_id=post.id)

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect(f'/cities/{post.city.id}')
