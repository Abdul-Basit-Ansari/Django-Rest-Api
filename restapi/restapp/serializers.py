from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework import serializers
from . models import Students

class StudentSrializers(serializers.ModelSerializer):
    marks = serializers.IntegerField()

    # def create(self , validated_data):
    #     Students.objects.create(**validated_data)
    class Meta:
        model = Students
        fields  = '__all__'
		
