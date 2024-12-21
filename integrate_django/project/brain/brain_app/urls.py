from django.urls import path,include
from brain_app import views
from django.conf.urls.static import static
from brain import settings
from django.contrib import admin


urlpatterns = [
    path('ten-brain-eeg-headband', views.ten_brain_eeg_headband),
    path('aboutus', views.aboutus),
    path('blogs', views.blogs),
    path('blog_view/<pk>', views.blog_view),
    path('contactus',views.contactus),
    path('synapse',views.synapse),
    path('flexcap-setup',views.flexcap_setup),
    path('privacy_policy',views.privacy_policy),
    path('return_policy',views.return_policy),
    path('disclaimer',views.disclaimer),
    path('terms_condition',views.terms_condition),
    path('ten_brain_eeg_flexcap',views.ten_brain_eeg_flexcap),
    path('faq',views.faq),
    path('',views.index),
    path('refund_policy',views.refund_policy),
    path('site_links', views.site_links),
    path('testimonials-and-reviews', views.testimonials_and_reviews),
    path('how_it_works',views.how_it_works),
    path('metal_health_podcast', views.metal_health_podcast),
    path('ten_brain_exg_synapse',views.ten_brain_exg_synapse),
    path('neuroscience_kits',views.neuroscience_kits),
    path('submit_subscription',views.submit_subscription),

    path('diy-neuroscience-kits-exg-synapse',views.diy_neuroscience_kits_exg_synapse),
    path("summernote/", include("django_summernote.urls")), # add this

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     # urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#     urlpatterns = [    
#       path("admin/", admin.site.urls),    
#       path("summernote/", include("django_summernote.urls")), # add this
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)