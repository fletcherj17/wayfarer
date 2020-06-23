from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile, City, Post
from django.core.paginator import Paginator



# Create your views here.
def home(request):
    error_message = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST) 
        if form.is_valid():
<<<<<<< HEAD
            current_city = form.cleaned_data ['current_city']
            name = form.cleaned_data ['name']
=======
            name = form.cleaned_data ['name']
            current_city = form.cleaned_data ['current_city'] 
>>>>>>> submaster
            user = form.save()
            Profile.objects.create(user=user, name=name, current_city=current_city)
            login(request,user)
            return redirect('profile')
        else:
            error_message = 'Invalid form'
    else:
        form = SignUpForm() 
    context = {'form': form, 'error_message': error_message}
    return render(request, 'home.html', context)


def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('profile')
    else:
        return render(request,'home.html',{'error':'Invalid Username or Password'})

def loginreq(request):
    return render(request,'home.html',{'error1': True})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
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

# Length validator
def length_validator(title,content):
        if title == '':
            return "This title is too short. It must contain at least 1 character."
        elif content == '':
            return "Content can not be blank"
        else:
            return False

@login_required
def show_city(request,city_id):
    cities = City.objects.all()
    city = City.objects.get(id=city_id)
    posts = Post.objects.filter(city=city_id).order_by('-date')
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        city = City.objects.get(pk=city_id) 
        author = request.user
        if (length_validator(title,content)):
            error_message = length_validator(title,content)
            context = {'city':city, 'posts':posts,'cities':cities,'page':page, 'error': error_message}
            return render(request, 'cities.html', context)
        else:
            post = Post.objects.create(title=title,content=content,city=city,author=author)
            post.save()
            return redirect('show_city', city_id=city.id)
    else:
        context = {'city':city, 'posts':posts,'cities':cities,'page':page}
        return render(request,'cities.html',context)

@login_required
def show_post(request, post_id):
    post = Post.objects.get(id=post_id)

    context = {'post': post,'user':request.user}
    return render(request, 'profile/show_post.html', context)

@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.save()
    return redirect('show_post', post_id=post.id)

@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect(f'/cities/{post.city.id}')
   
        