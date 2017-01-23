from django.db import models
from django import forms
from django.contrib.auth.models import User


class User_info(models.Model):
    user = models.OneToOneField(User)
    balance = models.IntegerField()
    aggregate = models.IntegerField()
    canSendNum = models.IntegerField()


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y%m/%d')


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )

class SendUser(models.Model):
    name = models.CharField(max_length=12)
    phone = models.IntegerField()

class SendUserForm(forms.ModelForm):
    class Meta:
        model = SendUser
        fields = []
