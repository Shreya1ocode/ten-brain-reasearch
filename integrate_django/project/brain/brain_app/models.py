from django.db import models
from datetime import datetime

# Create your models here.
class Contacts(models.Model):
    name=models.CharField(max_length=50,blank=True, null=True)
    email=models.EmailField()
    mobile=models.BigIntegerField(blank=True, null=True)
    country = models.CharField(max_length=255,blank=True, null=True) 
    message=models.CharField(max_length=255,blank=True, null=True)

class Blog(models.Model):
    blog_title=models.TextField()
    blog_description=models.TextField()
    blog_image = models.ImageField(blank=True, null=True)
    created_at = models.DateField(default=datetime.now)
    updated_at = models.DateField(default=datetime.now)
    
    @property
    def html_stripped(self):
        from django.utils.html import strip_tags
        return strip_tags(self.blog_title)