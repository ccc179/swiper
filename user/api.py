from django.http import HttpResponse
from django.shortcuts import render
from lib import sms

# Create your views here.
def submit_phone(request):
    """获取短信验证码"""
    if not request.method == "POST":
        return HttpResponse("request error")
    else:
        phone = request.POST.get('phone')
        print(phone)
        result, msg = sms.send_sms(phone)
        print(msg)
        return HttpResponse("send success")


def submit_vcode(request):
    """创建手机号"""
    pass


def get_profile(request):
    """创建手机号"""
    pass


def set_profile(request):
    """创建手机号"""
    pass


def upload_avatar(request):
    """创建手机号"""
    pass