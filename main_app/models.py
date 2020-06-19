from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    current_city = models.CharField(max_length=50, blank=False)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.current_city

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    

    
    