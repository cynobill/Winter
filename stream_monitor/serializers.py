from rest_framework import serializers
from stream_monitor.models import Artist, Track, Release
from stream_monitor.models import Project, Target, Session, Hit

from django.db import models

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id','name',)

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'title', 'artist', 'release')

class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = ('id','title',)




class HitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hit
        fields = ('id','time','session','track')


class SessionSerializer(serializers.ModelSerializer):
    hits = HitSerializer(many=True, read_only=True)
    class Meta:
        model = Session
        fields = ('id','target','url','start','stop', 'hits')


class TargetSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)
    class Meta:
        model = Target
        fields = ('id','name','project', 'sessions')


class ProjectSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True, read_only=True,)
    class Meta:
        model = Project
        fields = ('id','name','targets')
