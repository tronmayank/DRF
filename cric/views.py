from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from fastapi import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from cric.serializers import SingerSerializer

from .models import singer, songs, Tags,comments,User
# Create your views here.

class SingerView(APIView):
    
    def get(self, request):
        
        singerobj = singer.objects.all()
       
        
        serializer = SingerSerializer(singerobj, many=True) 
        print(serializer.data)
        #return HttpResponse('hello')
        return Response(serializer.data)