from decimal import Decimal
from django.conf import settings
from app.models import *

class Cart(object):
    def __init__(self,request):
        self.session=request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart=self.session[settings.CART_SESSION_ID]={}
        self.cart=cart

    def __iter__(self):
        tovar_ids=self.cart.keys()
        tovars=Tovar.objects.filter(id__in=tovar_ids)
        cart=self.cart.copy()
        for tovar in tovars:
            cart[str(tovar.id)]['tovar']=tovar
        for item in cart.values():
            item['price']=Decimal(item['price'])
            item['total_price']=item['price']*item['quantity']
            yield item
        return sum(item['quantity']for item in self.cart.values())

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def add(self,tovar,quantity=1,update_quantity=False):
        id=str(tovar.id)
        if id not in self.cart:
            self.cart[id]={'quantity':0,'price':str(tovar.price)}
        if update_quantity:
            self.cart[id]['quantity']=quantity
        else:
            self.cart[id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified=True

    def remove(self,tovar):
        id=str(tovar.id)
        if id in self.cart:
            del self.cart[id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

