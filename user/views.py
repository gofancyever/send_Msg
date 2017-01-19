# coding:utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import Document,DocumentForm
import os
from user import tool
from django.core.urlresolvers import reverse

def index(request):
    return render(request,'user/index.html')

def login(request):
    return render(request,'user/login.html')

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