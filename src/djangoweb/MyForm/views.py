from django.shortcuts import render

# Create your views here.
from MyForm import models
from django.template.loader import get_template

def form_index(request):
    return render(request, 'MyForm/index.html', locals())
