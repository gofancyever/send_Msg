from django.conf.urls import url
from commonality import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'index/$',views.index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)