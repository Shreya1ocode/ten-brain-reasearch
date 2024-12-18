from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('privacy/', views.privacy, name='privacy'),
    path('return/', views.returns, name='return'),
    path('reviews/', views.reviews, name='reviews'),
    path('tc/', views.tc, name='tc'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('blog/', views.blogs, name='blog'),
    path('desktop/', views.desktop, name='desktop'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('setup/',views.setup, name='setup'),
    path('flexcap/',views.flexcap, name='flexcap'),
    path('eeg-headband/',views.headband, name='headband'),
]


