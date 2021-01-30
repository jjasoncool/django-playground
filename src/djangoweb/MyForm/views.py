from django.shortcuts import render

# Create your views here.
from MyForm import models
from django.template.loader import get_template


def form_index(request):
    # 定義選單內容
    years = range(1960, 2021)
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


def message_index(request):
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()

    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['mood']

    except:
        user_id = None
        message = '如要張貼訊息,則每一個欄位都要填...'

    if user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message='成功儲存!請記得你的編輯密碼[{}]!,訊息需經審查後才會顯示。'.format(user_pass)

    return render(request, 'MyForm/message_board.html', locals())
