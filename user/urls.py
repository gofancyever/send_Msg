from django.conf.urls import url
from user import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^login',views.login),
    url(r'^logout',views.logout),
    url(r'^validityemail',views.validityemail),
    url(r'^sign',views.sign),
    url(r'^index/$',views.index),
    url(r'^testSend',views.upload_file, name='list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)