from django.conf.urls import url
from user import views


urlpatterns = [
    url(r'^login',views.login),
    url(r'^index/$',views.index),
    url(r'^testSend',views.upload_file, name='list'),
]