from django.shortcuts import render, Http404, HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from . serializers import *
import json
import datetime
from django.views.decorators.csrf import csrf_exempt
from math import sin, cos, sqrt, atan2, radians
from django.utils import timezone


def distance(la1, lo1, la2, lo2):

    R = 6373.0
    lat1 = radians(float(la1))
    lon1 = radians(float(lo1))
    lat2 = radians(float(la2))
    lon2 = radians(float(lo2))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    d = R * c
    return d


def sendtotab_algo(tab_id, latitude, longitude):


    obj = advertiser_data.objects.all()

    if Sendtotab.objects.filter(tab_id = tab_id).exists():

        a = Sendtotab.objects.get(tab_id = tab_id) 
        s = 0
        su=""
        for i in obj:
            d= distance(latitude, longitude, i.latitude, i.longitude)

            if d < float(i.radius):
                s = s+1
                su= su + i.video_id +" "
            if s > 21:
                break
                
        a.video_id = su
        a.time=timezone.now()
        a.save() 
    else:
        a = Sendtotab() 
        s = 0
        su=""
        for i in obj:

            d= distance(latitude, longitude, i.latitude, i.longitude)

            if d < float(i.radius):
                s = s+1
                su= su + i.video_id +" "
            if s > 21:
                break
        a.tab_id=tab_id      
        a.video_id = su
        a.save()          



@csrf_exempt
def update_tablocation(request):
    if request.method == "POST":
        post = json.loads(request.body.decode("utf-8"))
        print(post)
        response_data = {}
        if post.get("key") == "70b66a89929e93416d2ef535893ea14da331da8991cc7c74010b4f3d7fabfd62":
            tab_id = post['tab_id']
            latitude = post['latitude']
            longitude = post['longitude']
            

            sendtotab_algo(tab_id, latitude, longitude)


            try:

                if tablocation_model.objects.filter(tab_id = tab_id).exists():

                    a = tablocation_model.objects.get(tab_id = tab_id)
                    a.tab_id= tab_id
                    a.latitude= latitude
                    a.longitude= longitude
                    a.time=timezone.now()
                    a.save()
                    response_data['status'] = 'true'


                else:
                    a = tablocation_model()
                    a.tab_id= tab_id
                    a.latitude= latitude
                    a.longitude= longitude
                    a.save()
                    response_data['status'] = 'true'

            except Exception as e:
                    response_data['status'] = str(e)
                    print(e)
        else:
            response_data['status'] = 'Request Invalid'

        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
            )
    else:
        raise Http404("NOT ALLOWED")



@csrf_exempt
def update_video_count(request):
    if request.method == "POST":
        post = json.loads(request.body.decode("utf-8"))
        print(post)
        response_data = {}
        if post.get("key") == "70b66a89929e93416d2ef535893ea14da331da8991cc7c74010b4f3d7fabfd62":
            tab_id = post['tab_id']
            video_id = post['video_id']
            video_count = post['video_count']
    
            try:

                if video_count_model.objects.filter(tab_id = tab_id).exists():
                    a = video_count_model.get(tab_id = tab_id)
                    a.tab_id= tab_id
                    a.video_count= video_count
                    a.video_id= video_id
                    a.time=timezone.now()
                    a.save()
                    response_data['status'] = 'true'
                else:
                    a = video_count_model()
                    a.tab_id= tab_id
                    a.video_count= video_count
                    a.video_id= video_id
                    a.save()
                    response_data['status'] = 'true'

            except Exception as e:
                    response_data['status'] = str(e)
                    print(e)

        else:
            response_data['status'] = 'Request Invalid'

        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
            )
    else:
        raise Http404("NOT ALLOWED")


@csrf_exempt
def update_tab_running_status(request):
    if request.method == "POST":
        post = json.loads(request.body.decode("utf-8"))
        print(post)
        response_data = {}
        if post.get("key") == "70b66a89929e93416d2ef535893ea14da331da8991cc7c74010b4f3d7fabfd62":
            user_id = post['user_id']
            speed = post['speed']
            video_frquency = post['video_frquency']
            
            try:
                a = tab_running_status_model()
                a.user_id= user_id
                a.speed= speed
                a.video_frquency= video_frquency
                
                a.save()
                response_data['status'] = 'true'
            except Exception as e:
                    response_data['status'] = str(e)
                    print(e)

        else:
            response_data['status'] = 'Request Invalid'

        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
            )
    else:
        raise Http404("NOT ALLOWED")



class current_video_id(APIView):

   def get(self, request):
    
      allpost = Sendtotab.objects.all()
      serializer = current_video_idserializer(allpost, many=True)
      return Response(serializer.data)

   def post(self):
      pass

class downloadvideo(APIView):

   def get(self, request):
    
      allpost = download.objects.order_by('-time')
      serializer = downloadvideoserializer(allpost, many=True)
      return Response(serializer.data)

   def post(self):
      pass



class map_tablocation(APIView):

   def get(self, request):
    
      allpost = tablocation_model.objects.order_by('-time')
      serializer = map_tablocationserializer(allpost, many=True)
      return Response(serializer.data)

   def post(self):
      pass



#allpost = Information.objects.order_by('android_id', '-time')