from django import forms


class SendMsgForm(forms.Form):
    send_content = forms.CharField(required=False)
    send_phone = forms.CharField(required=False)
    send_name = forms.CharField(required=False)
    send_time = forms.DateField(required=False)
