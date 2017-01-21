from django.conf.urls import url
from user import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import (
    password_change,
    password_change_done,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)




urlpatterns = [
    url(r'^login',views.login),#登录
    url(r'^logout',views.logout),#登出
    url(r'^validityemail',views.validityemail),#验证邮箱
    url(r'^sign',views.sign),#注册
    url(r'^index/$',views.index),#主页
    # url(r'^forgetpassword/$',views.forgetpassword),#忘记密码


    url(r'^password_change/$', password_change,
        {
            'template_name': 'user/password_change_form.html',
            'post_change_redirect': 'users_password_change_done'
        },
        name='users_password_change'),
    url(r'^password_change/done/$', password_change_done,
        {'template_name': 'user/password_change_done.html'},
        name='users_password_change_done'),
    url(r'^password_reset/$', password_reset,
        {
            'template_name': 'user/password_reset_form.html',
            'email_template_name': 'user/password_reset_email.html',
            'subject_template_name': 'user/password_reset_subject.html',
            'post_reset_redirect': 'users_password_reset_done'
        },
        name='users_password_reset'),
    url(r'^password_reset/done/$', password_reset_done,
        {'template_name': 'user/password_reset_done.html'},
        name='users_password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm,
        {
            'template_name': 'user/password_reset_confirm.html',
            'post_reset_redirect': 'users_password_reset_complete'
        },
        name='users_password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete,
        {'template_name': 'user/password_reset_complete.html'},
        name='users_password_reset_complete'),



    url(r'^testSend',views.upload_file, name='list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)