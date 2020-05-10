#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import time
import requests
import urllib3

urllib3.disable_warnings()
sid ='V02******'#签到用户的sid
# sid = "V02SVweWGraVo68dHBZbuxBtUf0OCQs00a165bbb003a5b8c18"
url = "https://zt.wps.cn/2018/clock_in/api/clock_in?member=wps"
headers={
    'Host': 'zt.wps.cn',
    'content-type' : 'application/json',
    'sid' : sid
}
def func():
    r =requests.get(url,headers=headers,verify=False)
    # print(url)
    html = json.loads(r.text)
    if html['result']=='ok':
        print(html['result']+"---wps会员签到----------打卡成功！----------"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    else:
        print(html['result']+'原因：'+html['msg']+"----------"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print("开始执行，当前时间："+time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime())+" 每天签到时间为：8:00:00")
# while True:
#     time_now = time.strftime("%H:%M:%S", time.localtime())  # 刷新
#     if time_now == "8:00:00":  # 此处设置每天定时的时间
#         # 此处3行替换为需要执行的动作
#         func()
#         time.sleep(2)  # 因为以秒定时，所以暂停2秒，使之不会在1秒内执行多次
func()

