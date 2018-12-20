from rest_framework import serializers
from api.models import *


class current_video_idserializer(serializers.ModelSerializer):
   class Meta:
      model = Sendtotab
      fields= ('tab_id','video_id',)


class downloadvideoserializer(serializers.ModelSerializer):
   class Meta:
      model = download
      fields= ('city','video_id',)

class map_tablocationserializer(serializers.ModelSerializer):
   class Meta:
      model = tablocation_model
      fields= ('tab_id','latitude','longitude','time',)








