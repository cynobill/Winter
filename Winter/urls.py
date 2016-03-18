"""Winter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework_nested import routers
from stream_monitor import views

#router = routers.DefaultRouter()
#router.register(r'artists', views.ArtistViewSet)
#router.register(r'tracks', views.TrackViewSet)
#router.register(r'releases', views.ReleaseViewSet)
#router.register(r'projects', views.ProjectViewSet)
#router.register(r'targets', views.TargetViewSet)
#router.register(r'sessions', views.SessionViewSet)
#router.register(r'hits', views.HitViewSet)
#router.register(r'test', views.TestViewSet)

router = routers.DefaultRouter()
router.register(r'project', views.ProjectViewSet)

project_router = routers.NestedSimpleRouter(router, r'project', lookup='project')
project_router.register(r'target', views.TargetViewSet)

target_router = routers.NestedSimpleRouter(project_router, r'target', lookup='target')
target_router.register(r'session', views.SessionViewSet)

session_router = routers.NestedSimpleRouter(target_router, r'session', lookup='session')
session_router.register(r'hit', views.HitViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(project_router.urls)),
    url(r'^', include(target_router.urls)),
    url(r'^', include(session_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


'''
## music_id config

from django.conf.urls import url, include
from rest_framework import routers
from music_id import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

## original config

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^music_id/', include( 'music_id.urls' )),
    url(r'^admin/', admin.site.urls),
]
'''
