from django.db import models
from accounts.models import *
from django.utils import timezone

# Create your models here.

class tablocation_model(models.Model):
    tab_id = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200) 
    time = models.DateTimeField(default=timezone.now)    
 

class video_count_model(models.Model):
    tab_id = models.CharField(max_length=200)
    video_count = models.CharField(max_length=200)
    video_id = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now)


class tab_running_status_model(models.Model):
    tab_id = models.CharField(max_length=200)
    speed = models.CharField(max_length=200)
    video_frquency = models.CharField(max_length=200) 
    time = models.DateTimeField(default=timezone.now) 


class Sendtotab(models.Model):
    tab_id = models.CharField(max_length=200)
    video_id = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now)



class advertiser_data(models.Model):
    
    video_id = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    radius = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    area_name= models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now)


class select_location(models.Model):
    area_name= models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    radius = models.CharField(max_length=200)
    city = models.CharField(max_length=200)


class video_status_model(models.Model):
    
    username = models.CharField(max_length=200)
    video_id = models.CharField(max_length=200)
    verification_status= models.CharField(max_length=200)
    play_status = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now)


class download(models.Model):
    
    city = models.CharField(max_length=200)
    video_id = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now)

class advertiser_profile_model(models.Model):

    username = models.CharField(max_length=200)
    company_name= models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=200)
    company_address= models.CharField(max_length=200)



class hostad_money_model(models.Model):
    
    username = models.CharField(max_length=200)
    hostad_money= models.CharField(max_length=200)

class play_charges_model(models.Model):
    
    pay_per_play_charge= models.CharField(max_length=200)

class order_transaction_model(models.Model):
    
    username = models.CharField(max_length=200)
    oreder_id = models.CharField(max_length=200)
    order_status = models.CharField(max_length=200)
    about_order = models.CharField(max_length=200)
    order_amount = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now)







                
                