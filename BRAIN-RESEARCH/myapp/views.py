
from django.shortcuts import render

def home(request):
 return render(request, 'index.html')

def privacy(request):
    return render(request, 'Privacy.html')

def returns(request):
    return render(request, 'Return.html')

def reviews(request):
    return render(request, 'Reviews_and_testimonial.html')

def tc(request):
    return render(request, 't_and_c.html')

def disclaimer(request):
    return render(request, 'disclaimer.html')


def blogs(request):
    return render(request, 'blogs.html')

def desktop(request):
    return render(request, 'desktop_app.html')