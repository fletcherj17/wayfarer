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
    url = models.CharField(max_length=100)
   

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200,blank = False, null = False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank = False, null = False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering: ('-date',)
        
    def __str__(self):
        return self.title


    

    
    