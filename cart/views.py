from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from app.models import Tovar
from .cart import Cart
from .forms import AddProductForm

@require_POST
def cart_add(request, id):
    cart = Cart(request)
    if request.user.is_authenticated:
        product = get_object_or_404(Tovar, id=id)
        form = AddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(tovar=product, quantity=1)
        print(cart)
    else:
        return redirect('reg')
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    print(cart.__dict__)
    return render(request, 'cart/detail.html', {'cart': cart})