from rest_framework import serializers
from .models import *
from rest_framework.exceptions import APIException


class StatistikaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistika
        fields = '__all__'


    def validate_nasiya(self,nasiya):
        if nasiya > 500000:
            raise serializers.ValidationError("Mahsulot olib ketishingiz mumkin emas!")
        return nasiya