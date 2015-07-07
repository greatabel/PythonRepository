#coding: utf-8
import requests

def send_request(url):
    r = requests.get(url)
    return r.status_code

def visitdouban():
    t = send_request('http://www.douban.com')
    print("in visitdouban()",t)
    return t

