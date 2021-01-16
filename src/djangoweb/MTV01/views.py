from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from MTV01.models import Product


def about(request):
    html = '''<!DOCTYPE html>
    <html><head><title>About Myself</title></head>
    <body><h2>Andy Wood</h2><hr>
    <p>Hi, I am Andy Wood. Nice to meet you!</p>
    </body>
    </html>
    '''
    return HttpResponse(html)


def listing(request):

    html = '''
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset='utf-8'>
    <title>中古機列表</title>
    </head>
    <body>
    <h2>以下是目前本店販售中的二手機列表</h2>
    <hr>
    <table width=400 border=1 bgcolor='#ccffcc'>
    {}
    </table>
    <h2>以下是缺貨列表</h2>
    <hr>
    <table width=400 border=1 bgcolor='#ccffcc'>
    {}
    </table>
    </body>
    </html>
    '''

    products = Product.objects.all().order_by('-price').exclude(qty=0)
    tags = '<tr><td>品名</td><td>售價</td><td>庫存量</td></tr>'
    for p in products:
        tags += '<tr><td>{}</td>'.format(p.name)
        tags += '<td>{}</td>'.format(p.price)
        tags += '<td>{}</td></tr>'.format(p.qty)

    outOfStocks = Product.objects.filter(qty=0)
    out = '<tr><td>品名</td><td>售價</td><td>庫存量</td></tr>'
    for p in outOfStocks:
        out += '<tr><td>{}</td>'.format(p.name)
        out += '<td>{}</td>'.format(p.price)
        out += '<td>{}</td></tr>'.format(p.qty)

    return HttpResponse(html.format(tags, out))
