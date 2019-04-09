from django.shortcuts import render
from lib import sms
from lib.http import render_json
from common import errors


# Create your views here.
def submit_phone(request):
    """获取短信验证码"""
    if not request.method == "POST":
        return render_json("request error",code=errors.REQUEST_ERROR)
    else:
        phone = request.POST.get('phone')
        result, msg = sms.send_sms(phone)
        return render_json(msg)


def submit_vcode(request):
    """通过验证码登录注册"""
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
