from miniapp.models import product
from django.shortcuts import render, redirect, get_object_or_404
from .models import cart, items
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



@login_required
def add_cart(request, product_id):
    prod = get_object_or_404(product, id=product_id)
    user = request.user

    try:
        ct = cart.objects.get(user=user)
    except cart.DoesNotExist:
        ct = cart.objects.create(user=user)
    
    try:
        c_item = items.objects.get(prod=prod, cart=ct)
        if c_item.quan < c_item.prod.stock:
            c_item.quan += 1
        c_item.save()
    except items.DoesNotExist:
        c_item = items.objects.create(prod=prod, quan=1, cart=ct)
    
    return redirect('cart_details')


@login_required
def cart_details(request):
    user = request.user
    try:
        ct = cart.objects.get(user=user)
        ct_items = items.objects.filter(cart=ct, active=True)
        tot = sum(item.prod.price * item.quan for item in ct_items)
        count = sum(item.quan for item in ct_items)
        return render(request, 'cart.html', {"ci": ct_items, 't': tot, 'cn': count})
    except ObjectDoesNotExist:
        return HttpResponse("<script>alert('empty cart');window.location.href='/';</script>")


@login_required
def increment_item(request, item_id):
    item = get_object_or_404(items, id=item_id)
    if item.quan < item.prod.stock:
        item.quan += 1
        item.save()
    return redirect('cart_details')


@login_required
def decrement_item(request, item_id):
    item = get_object_or_404(items, id=item_id)
    if item.quan > 1:
        item.quan -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart_details')


@login_required
def delete_item(request, item_id):
    item = get_object_or_404(items, id=item_id)
    item.delete()
    return redirect('cart_details')
