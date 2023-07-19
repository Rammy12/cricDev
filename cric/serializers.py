from rest_framework import serializers
from .models import odis,t20men, ipl


class odisSerializer(serializers.ModelSerializer):
    class Meta:
        model=odis
        fields="__all__"



class t20Serializer(serializers.ModelSerializer):
    class Meta:
        model=t20men
        fields="__all__"


class iplSerializer(serializers.ModelSerializer):
    class Meta:
        model=ipl
        fields="__all__"