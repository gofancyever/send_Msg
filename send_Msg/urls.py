
from django.conf.urls import  include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^user/', include('user.urls')),
]