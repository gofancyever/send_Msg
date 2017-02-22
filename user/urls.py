from django.conf.urls import url
from user import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^/',views.index),
    url(r'^login',views.login),#登录
    url(r'^logout',views.logout),#登出
    url(r'^validityemail',views.validityemail),#验证邮箱
    url(r'^sign',views.sign),#注册
    url(r'^index/$',views.index),#主页
    url(r'^sendmsg/$',views.sendMsg),#发送信息
    # url(r'^forgetpassword/$',views.forgetpassword),#忘记密码


    url(r'^upload',views.upload_file, name='list'),

    url(r'^test/$',views.test),#发送信息
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)