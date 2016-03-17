from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^v1/', include( 'music_id.api_urls' )),
    url(r'^$',views.main_view, name='music_id_main'),
]