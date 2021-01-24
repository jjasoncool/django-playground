from django.shortcuts import render

# Create your views here.
from Modal_DB import models


def index(request):
    products = models.Product.objects.all()
    return render(request, 'Modal_DB/index.html', locals())


def db_detail(request, id):
    try:
        product = models.Product.objects.get(id=id)
        images = models.PPhoto.objects.filter(product=product)
    except:
        pass
    return render(request, 'Modal_DB/detail.html', locals())
