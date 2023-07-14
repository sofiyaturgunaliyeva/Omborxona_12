from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import *
from django.contrib.auth import authenticate, login, logout
# from userapp.models import Ombor
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import *
from rest_framework import status, filters
from django.contrib.postgres.search import TrigramSimilarity
from rest_framework_simplejwt.authentication import JWTAuthentication



class MijozModelViewset(ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializer
    authentication_classes = [JWTAuthentication]  # JSON Web token
    permission_classes = [IsAuthenticated]

class MahsulotModelViewset(ModelViewSet):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer
    authentication_classes = [JWTAuthentication]  # JSON Web token
    permission_classes = [IsAuthenticated]


