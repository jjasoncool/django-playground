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
from django.urls import include, path
from mainsite.views import homepage
from MTV01.views import about, listing, disp_detail
from URLS.views import homepage as url_home, about as url_about

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
    path('URLS/about/', url_about),
    path('URLS/about/<int:author_no>', url_about),
]
