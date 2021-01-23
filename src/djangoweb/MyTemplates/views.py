from django.shortcuts import render
from datetime import datetime

# Create your views here.


def index(request):
    msg = 'Hello'
    now = datetime.now()
    return render(request, 'MyTemplates/index.html', locals())


def tv(request, tvid=0):
    tv_list = [
        {'name': '東森', 'tvcode': 'RaIJ767Bj_M'},
        {'name': '民視', 'tvcode': 'XxJKnDLYZz4'},
        {'name': '台視', 'tvcode': 'yk2CUjbyyQY'},
        {'name': '華視', 'tvcode': 'TL8mmew3jb8'},
    ]
    now = datetime.now()
    tv = tv_list[tvid]
    return render(request, 'MyTemplates/tv.html', locals())
