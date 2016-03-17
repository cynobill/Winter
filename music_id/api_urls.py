from django.conf.urls import url

from . import views, api

urlpatterns = [
    url(r'^$',views.api_view, name='api_v1_view'),
    url(r'^project/(?P<project_id>[0-9]+)$',api.project, name='api_project_call')

]