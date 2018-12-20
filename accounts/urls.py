from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.user_login, name='first'),
    url(r'^logout/$', views.user_logout, name='log_out'),
    
]
