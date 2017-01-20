# coding:utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from .models import Document,DocumentForm
import os
from user import tool
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm


'''========================================================='''
#首页
@login_required
def index(request):
    return render_to_response('user/index.html',locals())


'''========================================================='''
#登录
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('index')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render(request,'user/login.html')


'''========================================================='''
#注册
def sign(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = UserCreationForm()
    return render(request,'user/sign-up.html')



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