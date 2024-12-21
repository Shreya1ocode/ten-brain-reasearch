from django.contrib import admin
from .models import Contacts,Blog
from django_summernote.widgets import SummernoteWidget 
from django.db import models 

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile','email','country','message']

class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = { 
            models.TextField: {'widget': SummernoteWidget}, 
     } 

    list_display = ['id','html_stripped']
    

admin.site.register(Contacts,ContactAdmin)
admin.site.register(Blog,BlogAdmin)