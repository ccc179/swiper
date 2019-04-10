from django.shortcuts import render
from lib import sms
from lib.http import render_json
from common import errors
from django.core.cache import cache
from common import keys
from user.models import User


# Create your views here.
def submit_phone(request):
    """获取短信验证码"""
    if not request.method == "POST":
        '''每次都可以去lib里面的http调用render_json帮助返回json 
            这个函数要传一个msg和一个状态码code
        '''
        return render_json("request error",code=errors.REQUEST_ERROR)
    else:
        # 从post请求里面拿到手机号,将手机号交给send_sms函数去发短信.
        phone = request.POST.get('phone')
        result, msg = sms.send_sms(phone)
        print(result)
        return render_json(msg)


def submit_vcode(request):
    """通过验证码登录注册"""
    if not request.method == "POST":
        return render_json("request error",code=errors.REQUEST_ERROR)
    # 取得手机发的验证码/手机号
    phone = request.POST.get('phone')
    vcode = request.POST.get('vcode')
    # 取得缓存中的验证码
    cache_vcode = cache.get(keys.VCODE_KEY.format(phone))

    #对比验证码是否一致
    if vcode == cache_vcode:
        users,_ = User.objects.get_or_create(phonenum=phone)
        request.session['uid'] = users.id
        return render_json(users.to_string())
    else:
        return render_json('verify code error',errors.VCODE_ERROR)




def get_profile(request):
    """得到轮廓"""
    pass


def set_profile(request):
    """设置轮廓"""
    pass


def upload_avatar(request):
    """上传头像"""
    pass
