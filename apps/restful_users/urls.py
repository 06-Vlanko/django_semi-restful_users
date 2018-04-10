from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sendToDefault),
    url(r'^users/$', views.index),
    url(r'^users/new/$', views.new), #to create new users
    url(r'^users/(?P<user_id>\d+)/edit/$', views.edit), #edits a user's data
    url(r'^users/(?P<user_id>\d+)/$', views.show), #displays a user's data
    url(r'^users/create/$', views.create), #used to create new users
    url(r'^users/(?P<user_id>\d+)/destroy/$', views.destroy),
    url(r'^users/update', views.update)
]