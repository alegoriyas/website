"""
Definition of urls for music.

"""
#https:www.youtube.com/watch?v=mWofrhTwGWQ&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK&index=12
from django.conf.urls import url

from . import views
app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/712/
    url(r'^(?P<album_id>[0-9]+)$', views.detail, name='detail'),
]
