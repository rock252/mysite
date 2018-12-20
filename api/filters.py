from django.contrib.auth.models import User
from api.models import *
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Information
        fields = ['advertiser_name', ]