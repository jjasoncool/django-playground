from django.shortcuts import render
from django.http import HttpResponse
from .models import PostContent

# Create your views here.
def homepage(request):
    posts = PostContent.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + str(post)+"<br>")
        post_lists.append("<small>" + str(post.body) + "</small><br>")
    return HttpResponse(post_lists)
