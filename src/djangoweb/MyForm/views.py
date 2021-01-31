from django.shortcuts import render

# Create your views here.
from MyForm import models, forms
from django.template.loader import get_template
from django.core.mail import EmailMessage


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


def message_index(request, msgid=None, del_pass=None):
    posts = models.Post.objects.filter(
        enabled=True).order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()

    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['mood']

    except:
        user_id = None
        message = '如要張貼訊息,則每一個欄位都要填...'

    if del_pass and msgid:
        try:
            post = models.Post.objects.get(id=msgid)
        except:
            post = None

        if post:
            if post.del_pass == del_pass:
                post.delete()
                message = "資料刪除成功"
            else:
                message = "密碼錯誤"
        else:
            message = "查無資料"

    elif user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post.objects.create(
            mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message = '成功儲存!請記得你的編輯密碼[{}]!,訊息需經審查後才會顯示。'.format(user_pass)

    return render(request, 'MyForm/message_board.html', locals())


def posting(request):
    posts = models.Post.objects.filter(
        enabled=True).order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()
    try:
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        user_post = request.POST['user_post']
        user_mood = request.POST['mood']

    except:
        user_id = None
        message = '如要張貼訊息,則每一個欄位都要填...'

    if user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post.objects.create(
            mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message = '成功儲存!請記得你的編輯密碼[{}]!,訊息請至下方查詢。'.format(user_pass)

    return render(request, 'MyForm/posting.html', locals())


def formlist(request):
    posts = models.Post.objects.filter(
        enabled=True).order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()

    return render(request, 'MyForm/listing.html', locals())


def contact_form(request):
    if request.method == 'POST':
        # post 時，對資料做事
        form = forms.ContactForm(request.POST)
        # 後端驗證資料
        if form.is_valid():
            message = "感謝您的來信。"
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']
            mail_body = u'''
            網友姓名:{}
            居住城市:{}
            是否在學:{}
            反應意見:如下
            {}'''.format(user_name, user_city, user_school, user_message)
            email = EmailMessage(
                '來自【NTU亂亂賣】網站的網友意見',
                mail_body,
                user_email,
                # 管理員(你自己)的email
                [' my.email@gmail.com ']
            )
            email.send()
        else:
            message = "請檢查您輸入的資訊是否正確!"
    else:
        # 非 post，輸出表單樣式
        form = forms.ContactForm()

    return render(request, 'MyForm/contact.html', locals())
