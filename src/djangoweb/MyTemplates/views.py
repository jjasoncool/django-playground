from django.shortcuts import render
from datetime import datetime

# Create your views here.


def index(request):
    msg = 'Hello'
    now = datetime.now()
    hour = now.timetuple().tm_hour
    return render(request, 'MyTemplates/index.html', locals())


def tv(request, tvid=0):
    tv_list = [
        {'name': '東森', 'tvcode': 'RaIJ767Bj_M'},
        {'name': '民視', 'tvcode': 'XxJKnDLYZz4'},
        {'name': '台視', 'tvcode': 'yk2CUjbyyQY'},
        {'name': '華視', 'tvcode': 'TL8mmew3jb8'},
    ]
    now = datetime.now()
    tv = tv_list[tvid]
    return render(request, 'MyTemplates/tv.html', locals())


def engtv(request, tvid='0'):
    tv_list = [
        {'name': 'SkyNews', 'tvcode': '99U4CH_k5F0'},
        {'name': 'Euro News', 'tvcode': 'F-uW_IswLh8'},
        {'name': 'India News', 'tvcode': 'E7dbhET6_EA'},
        {'name': 'CCTV', 'tvcode': 'vCDDYb_M2B4'},
    ]
    now = datetime.now()
    tv = tv_list[int(tvid)]
    return render(request, 'MyTemplates/engtv.html', locals())


def carlist(request, makerid=0):
    car_maker = ['SAAB', 'Ford', 'Honda', 'Mazda', 'Nissan', 'Toyota']
    car_list = [
        [],
        ['Fiesta', 'Focus', 'Modeo', 'EcoSport', 'Kuga', 'Mustang'],
        ['Fit', 'Odyssey', 'CR-V', 'City', 'NSX'],
        ['Mazda3', 'Mazda5', 'Mazda6', 'CX-3', 'CX-5', 'MX-5'],
        ['Tida', 'March', 'Livina', 'Sentra', 'Teana', 'X-Trail', 'Juke', 'Murano'],
        ['Camry', 'Altis', 'Yaris', '86', 'Prius', 'Vios', 'RAV4', 'Wish']
    ]
    maker_name = car_maker[makerid]
    cars = car_list[makerid]
    return render(request, 'MyTemplates/carlist.html', locals())


def carprice(request, makerid=0):
    car_maker = ['Ford', 'Honda', 'Mazda']
    car_list = [
        [
            {'model': 'Fiesta', 'price': 203500, 'qty':2},
            {'model': 'Focus', 'price': 605000, 'qty':5},
            {'model': 'Mustang', 'price': 900000, 'qty':9},
        ],
        [
            {'model': 'Fit', 'price': 450000, 'qty':4},
            {'model': 'City', 'price': 150000, 'qty':31},
            {'model': 'NSX', 'price': 1200000, 'qty':15},
        ],
        [
            {'model': 'Mazda3', 'price': 329999, 'qty':6},
            {'model': 'Mazda5', 'price': 603000, 'qty':7},
            {'model': 'Mazda6', 'price': 850000, 'qty':1},
        ],
    ]
    maker_name = car_maker[makerid]
    cars = car_list[makerid]
    return render(request, 'MyTemplates/carprice.html', locals())
