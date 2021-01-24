"""djangoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, reverse
from mainsite.views import homepage
from MTV01.views import about, listing, disp_detail
from URLS.views import homepage as url_home, about as url_about, reverse_url
from MyTemplates.views import index as tp_index, tv, engtv, carlist, carprice
from Modal_DB.views import index as db_index, db_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    # app mainsite
    path('', homepage),
    # app MTV01
    path('MTV01/about/', about),
    path('MTV01/list/', listing),
    path('MTV01/list/<sku>/', disp_detail),
    # app URLS
    path('URLS/', url_home),
    path('URLS/',include([
        path('about/', url_about),
        path('about/<int:author_no>', url_about),
    ])),
    path('URLS/reverse/<int:yr>/<int:mon>/<int:day>/<int:post_num>/', reverse_url, name='reverse_path'),
    path('URLS/chgPath/<int:yr>/<int:mon>/<int:day>/<int:post_num>/', reverse_url, name='reverse_chgPath'),
    # MyTemplates
    path('MyTemplates/', tp_index),
    path('MyTemplates/tv/', tv, name='tv_url'),
    path('MyTemplates/tv/<int:tvid>/', tv, name='tv_url'),
    path('MyTemplates/engtv/', engtv, name='engtv_url'),
    path('MyTemplates/engtv/<int:tvid>/', engtv, name='engtv_url'),
    path('MyTemplates/carlist/', carlist, name='carlist_url'),
    path('MyTemplates/carlist/<int:makerid>/', carlist, name='carlist_url'),
    path('MyTemplates/carprice/', carprice, name='carprice_url'),
    path('MyTemplates/carprice/<int:makerid>/', carprice, name='carprice_url'),
    # Modal_DB
    path('Modal_DB/', db_index),
    path('Modal_DB/detail/<int:id>', db_detail, name = 'db_detail_url'),
]
