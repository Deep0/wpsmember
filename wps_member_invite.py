#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import time

import requests
import urllib3

urllib3.disable_warnings()
i=1
sids =['V02***************************']    #抓取到的sid
url = "https://zt.wps.cn/2018/clock_in/api/invite"
print('请输入userid:')
userid=input()
data = '{"invite_userid":"'+userid+'"}'
for sid in sids:
    headers={
        'Host': 'zt.wps.cn',
        'content-type' : 'application/json',
        'sid' : sid ,
        'Accept-Encoding': 'gzip, deflate'
    }
    r = requests.post(url, headers=headers, data=data, verify=False)
    if r.status_code==200:
        if i<=10:
            html = json.loads(r.text)
            print(html['result'] + "增加成功！----------" + str(i))
            # print(sid)
            time.sleep(0.5)
            i = i+1
        else:
            break
    else:
        continue
