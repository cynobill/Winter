from stream_monitor.models import Artist, Track, Release
from stream_monitor.serializers import ArtistSerializer, TrackSerializer, ReleaseSerializer

from stream_monitor.models import Project, Target, Session, Hit
from stream_monitor.serializers import ProjectSerializer, TargetSerializer, SessionSerializer, HitSerializer

from rest_framework import viewsets, response
from django.shortcuts import get_object_or_404

class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows artists to be viewed or edited.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class TrackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tracks to be viewed or edited.
    """
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class ReleaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows releases to be viewed or edited.
    """
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TargetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows targets to be viewed or edited.
    """
    queryset = Target.objects.all()
    serializer_class = TargetSerializer

    def list(self, request, project_pk=None):
        print('List<-------------------------------------------------')
        queryset = Target.objects.filter(project=project_pk)
        serializer = TargetSerializer(queryset,context={'request': request}, many=True)
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None, project_pk=None):
        print('Retrieve<---------------------------------------------')
        queryset = Target.objects.filter(pk=pk, project=project_pk)
        target = get_object_or_404(queryset, pk=pk)
        serializer = TargetSerializer(target,context={'request': request})
        return response.Response(serializer.data)


class SessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sessions to be viewed or edited.
    """
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def list(self, request, project_pk=None, target_pk=None):
        print('List<-------------------------------------------------')
        queryset = Session.objects.filter(target__project=project_pk,target=target_pk)
        serializer = SessionSerializer(queryset,context={'request': request}, many=True)
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None, project_pk=None, target_pk=None):
        print('Retrieve<---------------------------------------------')
        queryset = Session.objects.filter(pk=pk, target__project=project_pk,target=target_pk)
        target = get_object_or_404(queryset, pk=pk)
        serializer = SessionSerializer(target,context={'request': request})
        return response.Response(serializer.data)


class HitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows releases to be viewed or edited.
    """
    queryset = Hit.objects.all()
    serializer_class = HitSerializer

class TestViewSet(viewsets.ModelViewSet):
    """
    API endpoint for testing.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
