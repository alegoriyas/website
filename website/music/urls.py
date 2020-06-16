"""
Definition of urls for music.

"""
#https:www.youtube.com/watch?v=mWofrhTwGWQ&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK&index=12
from django.conf.urls import url

from . import views
app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/<album_id>/            pk=album_id
    url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),
]
