from django.shortcuts import render,HttpResponse,redirect
from brain_app.models import Contacts,Blog
# from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
def neuroscience_kits(request):
    return render(request,'neuroscience_kits.html')


def ten_brain_exg_synapse(request):
    return render(request,'ten_brain_exg_synapse.html')

def metal_health_podcast(request):
    return render(request, 'metal_health_podcast.html')

def how_it_works(request):
    return render(request,'how_it_works.html')



def testimonials_and_reviews(request):
    return render(request,'testimonials_and_reviews.html')

def site_links(request):
    return render(request,'site_links.html')

def refund_policy(request):
    return render(request,'refund_policy.html')

def index(request):
    context={}
    if request.method=='POST':
        uname=request.POST['uname']
        umail=request.POST['uemail']
        umob=request.POST['umobile']
        # ucountry = request.POST['ucountry']
        umsg=request.POST['umessage']
        # print(uname,'-',umail,'-',umob,'-',umsg)
        u=Contacts.objects.create(name=uname,email=umail,mobile=umob,message=umsg)        
        u.save()

        html_content = render_to_string(
            "my_email.html",
            context={"my_variable": 42},
        )
        text_content = strip_tags(html_content)
        # Then, create a multipart email instance.
        msg = EmailMultiAlternatives(
            "Submitted your query successfully",
            text_content,
            "debadritapaul76@gmail.com",
            [umail],
            headers={"List-Unsubscribe": "<mailto:unsub@example.com>"},
        )

        # Lastly, attach the HTML content to the email instance and send.
        msg.attach_alternative(html_content, "text/html")
        # print(msg)
        msg.send()


        # msg="We will contact you soon"
        # send_mail(
        #     "Submitted your query successfully",
        #     msg,
        #     "debadritapaul76@gmail.com",
        #     [umail],
        #     fail_silently=False,
        # ) 
        
        context['success_msg']='Your Query is successfully send to us.We will contact you soon'
        return render(request,'index.html',context)
    else:
        return render(request,'index.html')
    
    # return render(request,'index.html')

def ten_brain_eeg_flexcap(request):
    return render(request,'ten_brain_eeg_flexcap.html')

def faq(request):
    return render(request,'faq.html')

def disclaimer(request):
    return render(request, 'disclaimer.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms_condition(request):
    return render(request, 'terms_condition.html')

def return_policy(request):
    return render(request, 'return_policy.html')

def blogs(request):
    context = {}
    blog_list = Blog.objects.all().order_by('-id')
    context['blogs'] = blog_list
    return render(request, 'blogs.html',context)

def blog_view(request, pk):
    context = {}
    blog_one = Blog.objects.get(id=pk)
    context['blog'] = blog_one

    #get and show all blog
    blog_all = Blog.objects.all().exclude(id=pk)[:3]
    context['blog_all'] = blog_all

    # print(context)
    return render(request, 'blog_view.html',context)

def aboutus(request):
    return render(request,'aboutus.html')

def diy_neuroscience_kits_exg_synapse(request):
    return render(request,'diy_neuroscience_kits_exg_synapse.html')

def flexcap_setup(request):
    return render(request, 'flexcap_setup.html')

def synapse(request):
    return render(request,'synapse.html')

def ten_brain_eeg_headband(request):
    context={}
    if request.method=='POST':
        uname=request.POST['uname']
        umail=request.POST['uemail']
        umob=request.POST['umobile']
        ucountry = request.POST['ucountry']
        umsg=request.POST['umessage']
        # print(uname,'-',umail,'-',umob,'-',umsg)
        u=Contacts.objects.create(name=uname,email=umail,mobile=umob,message=umsg,country = ucountry)        
        u.save()

        html_content = render_to_string(
            "my_email.html",
            context={"my_variable": 42},
        )
        text_content = strip_tags(html_content)
        # Then, create a multipart email instance.
        msg = EmailMultiAlternatives(
            "Submitted your query successfully",
            text_content,
            "debadritapaul76@gmail.com",
            [umail],
            headers={"List-Unsubscribe": "<mailto:unsub@example.com>"},
        )

        # Lastly, attach the HTML content to the email instance and send.
        msg.attach_alternative(html_content, "text/html")
        # print(msg)
        msg.send()


        # msg="We will contact you soon"
        # send_mail(
        #     "Submitted your query successfully",
        #     msg,
        #     "debadritapaul76@gmail.com",
        #     [umail],
        #     fail_silently=False,
        # ) 
        
        context['success_msg']='Your Query is successfully send to us.We will contact you soon'
        return render(request,'ten_brain_eeg_headband.html',context)
    else:
        return render(request,'ten_brain_eeg_headband.html')
 

def contactus(request):
    context={}
    if request.method=='POST':
        uname=request.POST['uname']
        umail=request.POST['uemail']
        umob=request.POST['umobile']
        ucountry = request.POST['ucountry']
        umsg=request.POST['umessage']
        # print(uname,'-',umail,'-',umob,'-',umsg)
        u=Contacts.objects.create(name=uname,email=umail,mobile=umob,message=umsg,country = ucountry)        
        u.save()

        html_content = render_to_string(
            "my_email.html",
            context={"my_variable": 42},
        )
        text_content = strip_tags(html_content)
        # Then, create a multipart email instance.
        msg = EmailMultiAlternatives(
            "Submitted your query successfully",
            text_content,
            "debadritapaul76@gmail.com",
            [umail],
            headers={"List-Unsubscribe": "<mailto:unsub@example.com>"},
        )

        # Lastly, attach the HTML content to the email instance and send.
        msg.attach_alternative(html_content, "text/html")
        # print(msg)
        msg.send()


        # msg="We will contact you soon"
        # send_mail(
        #     "Submitted your query successfully",
        #     msg,
        #     "debadritapaul76@gmail.com",
        #     [umail],
        #     fail_silently=False,
        # ) 
        
        context['success_msg']='Your Query is successfully send to us.We will contact you soon'
        return render(request,'contactus.html',context)
    else:
        return render(request,'contactus.html')
    
    
def submit_subscription(request):
    context={}
    if request.method=='POST':
        umail=request.POST['uemail']
        page_url = request.POST['page_url']
        
        u=Contacts.objects.create(email=umail)        
        u.save()

        html_content = render_to_string(
            "my_email.html",
            context={"my_variable": 42},
        )
        text_content = strip_tags(html_content)
        # Then, create a multipart email instance.
        msg = EmailMultiAlternatives(
            "Submitted your subscribing successfully",
            text_content,
            "debadritapaul76@gmail.com",
            headers={"List-Unsubscribe": "<mailto:unsub@example.com>"},
        )

        # Lastly, attach the HTML content to the email instance and send.
        msg.attach_alternative(html_content, "text/html")
        # print(msg)
        msg.send()
        
        context['success_msg']='Your email is successfully subscribed to us.We will contact you soon'
        url = "/"+page_url
        return redirect(url)
    else:
        return render(request,'contactus.html')
    
    
