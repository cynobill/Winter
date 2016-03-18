from rest_framework import serializers
from stream_monitor.models import Artist, Track, Release
from stream_monitor.models import Project, Target, Session, Hit

from django.db import models

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('id','name',)

class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'title', 'artist', 'release')

class ReleaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Release
        fields = ('id','title',)

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id','name',)

class TargetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Target
        fields = ('id','name','project')

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ('id','target','start','url','stop')

class HitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hit
        fields = ('id','time','session','track')
