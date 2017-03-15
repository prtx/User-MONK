from django.conf.urls import url, include
from .api import Monk_ListAPIView, Monk_CreateAPIView, Monk_DetailAPIView, Monk_UpdateAPIView, Monk_DeleteAPIView

urlpatterns = [
    url(r'^$', Monk_ListAPIView.as_view(), name='list'),
    url(r'^new/$', Monk_CreateAPIView.as_view(), name='new'),
    url(r'^(?P<user>\d+)/$', Monk_DetailAPIView.as_view(), name='detail'),
    url(r'^(?P<user>\d+)/edit/$', Monk_UpdateAPIView.as_view(), name='update'),
    url(r'^(?P<user>\d+)/delete/$', Monk_DeleteAPIView.as_view(), name='delete'),
]