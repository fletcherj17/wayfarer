from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('cities/', views.cities,name='cities'),
    path('cities/<int:city_id>/', views.show_city, name='show_city'),
    path('profile/posts/<int:post_id>/', views.show_post, name='show_post'),
    path('cities/<int:city_id>/add_post/',views.add_post, name='add_post')
]