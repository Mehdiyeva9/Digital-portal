from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Collab(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="digit_imgs")

    def __str__(self):
        return self.name

class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=256)
    company = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
class Programs(models.Model):
    name = models.CharField(max_length=200)
    duration = models.CharField(max_length=25)
    image = models.ImageField(upload_to="digit_imgs")
    price = models.IntegerField(default=0)
    about = models.TextField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    reading_duration = models.CharField(max_length=25)
    content = HTMLField()
    count_of_seen = models.IntegerField(default=0)
    count_of_comment = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    
    def __str__(self):
        return self.content[:50]
    
class SiteSettings(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    