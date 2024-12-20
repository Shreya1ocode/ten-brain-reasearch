"""
URL configuration for myproject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  
    path('privacy/', include('myapp.urls')), 
    path('return/', include('myapp.urls')),  
    path('reviews/', include('myapp.urls')),  
    path('terms_conditions/', include('myapp.urls')),  
    path('disclaimer/', include('myapp.urls')),   
    path('blog/', include('myapp.urls')),   
    path('desktop/', include('myapp.urls')),
    path('aboutus/', include('myapp.urls')),
    path('setup/', include('myapp.urls')),
    path('flexcap/', include('myapp.urls')),
    path('refund/', include('myapp.urls')),
    path('sitelinks/', include('myapp.urls')),
    path('returns/', include('myapp.urls')),

        
]

