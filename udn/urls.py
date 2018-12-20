from django.conf.urls import url
from django.contrib import admin
from udn import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url( r'^contact/', views.contact, name='contact' ),
    url( r'^customer_portal1/$', views.customer_portal1, name='customer_portal1' ),
    url( r'^service/$', views.service, name='service' ),
    url( r'^features/$', views.features, name='features' ),
    url( r'^pricing/$', views.pricing, name='pricing' ),
    url( r'^team/$', views.team, name='team' ),
    url( r'^faq/$', views.faq, name='faq' ),
    url( r'^blog/$', views.blog, name='blog' ),
    url( r'^maps/$', views.maps, name='maps' ),
    url(r'^adv/$',views.advertiser_details,name='adv'),
    
    
]
