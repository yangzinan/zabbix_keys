#!/usr/bin/env python
# -*- coding: utf-8 -*-  
import os,sys  
import time  
import sys  
import pycurl 
import json
urllist=[['中台WEB', 'https://biz.kaslyju.net/kasly-web/kaptchaImage'], ['奖金查询', 'http://www.nv580.com/Code.php'], ['奖金查询备用', 'http://www1.nv580.com/Code.php'], ['微信接口', 'http://47.92.112.107/']]
class Test:
    def __init__(self):
        self.contents = ''
    def callback(self,curl):
        self.contents = self.contents + curl
def test_gzip(url):
    data = {} 
    t = Test() 
    c = pycurl.Curl()  
    c.setopt(pycurl.WRITEFUNCTION,t.callback)
    c.setopt(pycurl.ENCODING, 'gzip')
    c.setopt(pycurl.URL,url) 
    c.perform()    
    data['HTTP_CODE']=c.getinfo(c.HTTP_CODE)
    data['NAMELOOKUP_TIME']=(c.getinfo(c.NAMELOOKUP_TIME))*1000
    data['CONNECT_TIME']=(c.getinfo(c.CONNECT_TIME))*1000
    data['PRETRANSFER_TIME']=(c.getinfo(c.PRETRANSFER_TIME))*1000
    data['SPEED_DOWNLOAD']=c.getinfo(c.SPEED_DOWNLOAD) / 1024
    return data
def web_name_discovery():
    web_list=[]
    web_dict={"data":None}
    for url in urllist:
        url_dict={}
        url_dict["{#NAME}"]=url[0]
        url_dict["{#URL}"] = url[1]
        web_list.append(url_dict)
    web_dict["data"]=web_list
    jsonStr = json.dumps(web_dict, sort_keys=True, indent=4,ensure_ascii=False)
    return jsonStr
def get_web_status():
    data=test_gzip(sys.argv[2])
    return data[sys.argv[3]]
if __name__ == '__main__':
    if sys.argv[1] == "web_name_discovery":
        print web_name_discovery()
    elif sys.argv[1] == "get_web_status":
        print get_web_status()
