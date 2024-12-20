
from django.shortcuts import render

def home(request):
 return render(request, 'index.html')

def privacy(request):
    return render(request, 'Privacy.html')

def returns(request):
    return render(request, 'Return.html')

def reviews(request):
    return render(request, 'Reviews_and_testimonial.html')

def terms_conditions(request):
    return render(request, 'Terms-conditions.html')

def disclaimer(request):
    return render(request, 'disclaimer.html')


def blogs(request):
    return render(request, 'blogs.html')

def desktop(request):
    return render(request, 'desktop_app.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def setup(request):
    return render(request, 'set_up.html')

def flexcap(request):
    return render(request, 'flexcap.html')

def refund(request):
    return render(request, 'Refund.html')




