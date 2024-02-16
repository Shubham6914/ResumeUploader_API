from rest_framework import serializers
from .models import profile


class ProfileSerializers(serializers.ModelSerializer):
   class Meta:
      model = profile
      fields =  ['id','name','email','gender','DOB','state','location','pimage','rdoc']