from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Collab(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="digit_imgs")

    def __str__(self):
        return self.name
    
class OurService(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
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
    middle_title = models.CharField(max_length=100)
    middle_content = models.TextField()
    middle_title1 = models.CharField(max_length=100)
    middle_content1 = models.TextField()
    icon1 = models.ImageField(upload_to="digit_imgs")
    middle_title2 = models.CharField(max_length=100)
    middle_content2 = models.TextField()
    icon2 = models.ImageField(upload_to="digit_imgs")
    middle_title3 = models.CharField(max_length=100)
    middle_content3 = models.TextField()
    icon3 = models.ImageField(upload_to="digit_imgs")
    middle_title4 = models.CharField(max_length=100)
    middle_content4 = models.TextField()
    icon4 = models.ImageField(upload_to="digit_imgs")
    header_title = models.CharField(max_length=100)
    header_content = models.TextField()
    solution_title = models.CharField(max_length=150)
    solution_content = models.TextField()
    about_title = models.CharField(max_length=100)
    about_content = models.TextField()
    about_title1 = models.CharField(max_length=100)
    about_content1 = models.TextField()
    about_title2 = models.CharField(max_length=100)
    about_content2 = models.TextField()
    number = models.CharField(max_length=13)
    mail = models.EmailField(max_length=256)
    location = models.CharField(max_length=150)
    for_subscribe_email = models.EmailField(max_length=256)

    class Meta:
        verbose_name_plural = "Settings"

    def __str__(self):
        return "Settings"

    def save(self, *args, **kwargs):
        if not self.id and SiteSettings.objects.exists():
            pass
        return super(SiteSettings, self).save(*args, **kwargs)