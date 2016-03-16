from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.main_view, name='music_id_main'),
    url(r'^v1/',views.api_view, name='api_v1_view')
]