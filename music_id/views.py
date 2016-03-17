from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from music_id.models import Channel
from pprint import pprint

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from music_id.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class Calls:
    @classmethod
    def channel_get(cls, request):
        pprint(request.META)
        pprint(request.GET)
        return "GET request to channel object."

    @classmethod
    def session_get(cls):
        return "GET request to session object."


class API:
    call = {'channel': {'GET': Calls.channel_get},
            'session': {'GET': Calls.session_get}
           }


def main_view(request):
    for channel in Channel.objects.all():
        print('-----------------------------------------------')
        print(channel.channel+' @ '+channel.site)
        for session in channel.session_set.all():
            print('  Session start: '+str(session.start.ctime()))
            for hit in session.hit_set.all():
                print('    '+str(hit.time.strftime('%H:%M:%S'))+': '+hit.song.artist.name+" - "+hit.song.title+" ("+hit.song.release.title+")" )


        return HttpResponse("Hello shitheads!")

def api_view(request):
    http_method = request.method
    api_call = request.path.split('/')[3]

    try:
        call = API.call[api_call]
    except:
        return HttpResponse( "Invalid call: \""+api_call+"\" object not found.")

    try:
        response = call[http_method](request)
    except:
        return HttpResponse( "Invalid response: \""+api_call+"\" does not support the \""+http_method+"\" method.")

    return HttpResponse("Hello from the api! "+response)