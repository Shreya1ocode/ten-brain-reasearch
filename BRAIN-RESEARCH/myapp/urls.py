from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('privacy/', views.privacy, name='privacy'),
    path('return/', views.returns, name='return'),
    path('reviews/', views.reviews, name='reviews'),
    path('terms_conditions/', views.terms_conditions, name='terms_conditions'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('blog/', views.blogs, name='blog'),
    path('desktop/', views.desktop, name='desktop'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('setup/',views.setup, name='setup'),
    path('flexcap/',views.flexcap, name='flexcap'),
     path('refund/',views.refund, name='refund'),
    
     path('returns/',views.returns, name='returns'),
]


