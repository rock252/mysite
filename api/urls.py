from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tablocation/$',views.update_tablocation,name='tablocation'),
    url(r'^video_count/$',views.update_video_count,name='video_count'),
    url(r'^tab_running_status/$',views.update_tab_running_status,name='tab_running_status'),
    
]
