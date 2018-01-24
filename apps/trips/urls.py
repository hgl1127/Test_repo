from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^add_trip$', views.addtrip),
    url(r'^manageerrors$', views.manageerrors),
    url(r'^logout$', views.logout),
    url(r'^home$', views.home),
    url(r'^destination/(?P<trip_id>\d+)$', views.destination),
    url(r'^join/(?P<trip_id>\d+)$', views.join),
        ]
