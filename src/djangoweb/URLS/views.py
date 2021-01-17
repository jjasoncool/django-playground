from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    return HttpResponse("Hello world!")


def about(request, author_no=0):
    html = "<h2>Here is No:{}'s about page!</h2><hr>".format(author_no)
    return HttpResponse(html)

def reverse_url(request, yr, mon, day, post_num):
    return render(request, 'URLS/reverseURL.html', locals())
