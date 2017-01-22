# coding:utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from .models import Document,DocumentForm,User_info
import os
from user import tool
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
    return render_to_response('user/index.html',locals())


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

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            baseDir = os.path.dirname(os.path.abspath(__name__))
            filename = os.path.join(baseDir, newdoc.docfile.name)
            json = tool.loadxl(filename)
            return json

    else:
        form = DocumentForm()
    documents = Document.objects.all()
    return render(request, 'user/send-msg.html', {'form': form,'documents': documents})

'''========================================================='''
#发送信息
def sendMsg(request):
    if request.method == 'POST':
        #验证登录用户合法性
        if request.user.is_authenticated():
            #取当前用户可发送条数
            user = request.user
            msg = request.POST.get('msg')
            phone = request.POST.get('phone')
            name = request.POST.get('name')
            time = request.POST.get('time')

        #取发送内容


        #取发送联系人

        #发送

        #返回结果
            return JsonResponse({'msg':0}, safe=False)
    return JsonResponse({'msg':0}, safe=False)


def send_msg_privte(user,msg,phone,name,time):
    canSendNum = user.user_info.canSendNum
    #发送信息
    return 200