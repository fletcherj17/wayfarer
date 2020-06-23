from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loginreq/', views.loginreq, name='loginrequired'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('cities/<int:city_id>/', views.show_city, name='show_city'),
    path('profile/posts/<int:post_id>/', views.show_post, name='show_post'),
    path('profile/posts/<int:post_id>/edit/',views.edit_post, name='edit_post'),
    path('profile/posts/<int:post_id>/delete/',views.delete_post, name='delete_post')
]