# -*- coding: utf-8 -*-

from aliMsg.alidayu import AlibabaAliqinFcSmsNumSendRequest
import json

req = AlibabaAliqinFcSmsNumSendRequest(23650888,'66a590e04f15a90bb067524809b48abf')
req.sms_type = 'normal'
req.sms_free_sign_name = '推广'

params = {"code":"1234","product":"alidayu"}
req.sms_param=json.dumps(params)
req.rec_num = '18535584484'
req.sms_template_code = "SMS_49240026"

try:
    resp= req.getResponse()
    print(resp)
except Exception as e:
    print(e)