from rest_framework import serializers
from .models import *
from rest_framework.exceptions import APIException


class OmborSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ombor
        fields = '__all__'


