from django.shortcuts import render

# Create your views here.
from Modal_DB import models


def index(request):
    products = models.Product.objects.all()
    return render(request, 'Modal_DB/index.html', locals())
