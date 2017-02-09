# coding:utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render,render_to_response
from .models import Document,DocumentForm,User_info
import os
from user import tool
from user.form import SendMsgForm

from django.contrib import auth
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

'''========================================================='''
#首页
@login_required(login_url='/user/login/')
def index(request):
    return render_to_response('user/index.html')


'''========================================================='''
#登录
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/user/index/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/user/index/')
    else:
        return render(request,'user/login.html')

'''========================================================='''
#登出
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/user/login/')

'''========================================================='''
#注册
def sign(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/user/login/')
    else:
        form = UserCreationForm()
    return render(request,'user/sign-up.html')

'''========================================================='''
#验证邮箱
def validityemail(request):
    if request.method == 'GET':
        email = request.GET.get('email',None)
        user = User.objects.filter(email=email).first()
        if user is not None:
            return JsonResponse({'msg':1},safe=False)
        else:
            return JsonResponse({'msg':0}, safe=False)

'''========================================================='''
#忘记密码
def forgetpassword(request):
    pass

#上传文件
@login_required
def upload_file(request):
    if request.method == 'POST':
        newdoc = Document(docfile=request.FILES['file'])
        if newdoc is not None:
            # file is saved
            newdoc.save()
            baseDir = os.path.dirname(os.path.abspath(__name__))
            filename = os.path.join(baseDir, newdoc.docfile.name)
            dict = tool.loadxl(filename)
            # datas = dict['data']
            datas = [{'name': '双龙', 'phone': 18535584484.0}, {'name': '双龙', 'phone': 18535584484.0},
                     {'name': '双龙', 'phone': 18535584484.0}, {'name': '双龙', 'phone': 18535584484.0},
                     {'name': '双龙', 'phone': 18535584484.0}, {'name': '双龙', 'phone': 18535584484.0},
                     {'name': '双龙', 'phone': 18535584484.0}, {'name': '双龙', 'phone': 18535584484.0},
                     {'name': '双龙', 'phone': 18535584484.0}, {'name': '双龙', 'phone': 18535584484.0},
                     ]

            return render_to_response('user/index.html',{'datas':datas})
    else:
        return JsonResponse(tool.formatData(None,400,'提交数据未通过'),safe=False)
'''========================================================='''
#发送信息
def sendMsg(request):
    if request.method == 'POST':
        #验证登录用户合法性
        if request.user.is_authenticated():
            #取当前用户可发送条数
            user = request.user
            form = SendMsgForm(request.POST,request.FILES)
            if form.is_valid():
                cd = form.cleaned_data
                result = send_msg_privte(user,cd['send_content'],cd['send_phone'],cd['send_name'],cd['send_time'])
                return JsonResponse({'msg':result}, safe=False)
            return JsonResponse({'msg': 400}, safe=False)
        return JsonResponse({'msg': 401}, safe=False)
    return JsonResponse({'msg':402}, safe=False)


def send_msg_privte(user,msg,phone,name,time):
    canSendNum = user.user_info.canSendNum
    if not canSendNum>0 :
        return 300

    #发送信息
    return 200


def test(request):
    datas = [{'name': '双龙', 'phone': 18535584484.0}, {'name': '双龙', 'phone': 18535584484.0},
                      {'name': '双龙', 'phone': 18535584484.0}, {'name': '双龙', 'phone': 18535584484.0},
                      {'name': '双龙', 'phone': 18535584484.0}, {'name': '双龙', 'phone': 18535584484.0},
                      {'name': '双龙', 'phone': 18535584484.0}, {'name': '双龙', 'phone': 18535584484.0},
                      {'name': '双龙', 'phone': 18535584484.0}, {'name': '双龙', 'phone': 18535584484.0},
                      {'name': '双龙', 'phone': 18535584484.0}]
    return render(request, 'user/base_test.html',{'datas':datas})