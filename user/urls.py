from django.conf.urls import  url
from django.conf import settings
from django.conf.urls.static import static



from user import views

urlpatterns = [
    url(r'^login',views.login),
    url(r'^index',views.index),
    url(r'^testSend',views.upload_file, name='list'),
]