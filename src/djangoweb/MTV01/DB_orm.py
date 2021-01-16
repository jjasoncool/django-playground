from MTV01.models import Product
from django.db.models import Sum, Avg, Max, Min

Product.objects.all().delete()

Product.objects.create(sku='a01',name='尼多蘭',price=500,size='S',qty=5)
Product.objects.create(sku='a02',name='尼多娜',price=600,size='M',qty=3)
Product.objects.create(sku='a03',name='尼多后',price=800,size='L',qty=2)
Product.objects.create(sku='a04',name='尼多朗',price=550,size='S',qty=7)
Product.objects.create(sku='a05',name='尼多力諾',price=650,size='M',qty=4)
Product.objects.create(sku='a06',name='尼多王',price=1300,size='L',qty=2)
Product.objects.create(sku='p01',name='HTC Magic',price=100,size='S',qty=0)
Product.objects.create(sku='p02',name='SONY Xperia Z3',price=15000,size='S',qty=1)
Product.objects.create(sku='p03',name='Samsung DUOS',price=800,size='S',qty=2)
Product.objects.create(sku='p04',name='Nokia Xpress 5800',price=500,size='S',qty=1)
Product.objects.create(sku='p05',name='Infocus M370',price=1500,size='S',qty=2)

print(Product.objects.all().aggregate(Sum('price')))
