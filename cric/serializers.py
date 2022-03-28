from pyexpat import model
from attr import fields
from rest_framework import serializers
from .models import singer, songs, Tags, comments, User
from dataclasses import fields

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','email','password')



class SongSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = songs
        fields = ['id','title','duration','sungby','tags','createdAt','updatedAt']

class SingerSerializer(serializers.ModelSerializer):
    allsongs = SongSerializer(read_only = True, many=True)
    class Meta:
        model = singer
        fields = ['id', 'name', 'gender', 'age', 'allsongs','createdAt','updatedAt']

class TagsSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields=('id','title','user','createdAt','updatedAt')
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comments
        fields = ('id','user','comment','song','createdAt','updatedAt')



