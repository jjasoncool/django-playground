from django.shortcuts import render

# Create your views here.
from MyForm import models
from django.template.loader import get_template


def form_index(request):
    # 定義選單內容
    years = range(1960,2021)
    try:
        urid = request.GET['user_id']
        urpass = request.GET['user_pass']
        se_byear = request.GET['byear']
        urfcolor = request.GET.getlist('fcolor')
        radio_movie = request.GET['movie']

    except:
        urid = None

    if urid != None and urpass == '12345':
        verified = True
    else:
        verifeid = False

    return render(request, 'MyForm/index.html', locals())
