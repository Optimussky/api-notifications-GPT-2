#from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
#from .models import Notification
from notification.models import Login, Notification

class LoginSerializer(ModelSerializer):
    class Meta:
        model = Login
        #fields = '__all__' # Esto no es recomendable
        fields = ['username','password']

class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ['uuid', 'body', 'email', 'title']

