from django.shortcuts import render,get_object_or_404
from miniapp.models import product
from django.shortcuts import render, redirect
from .models import cart,items
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from miniapp.models import *



def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id

def add_cart(request,product_id):
    prod=product.objects.get(id=product_id)

    try:
        ct=cart.objects.get(cartid=c_id(request))      #if cart id exist
    except cart.DoesNotExist:
        ct=cart.objects.create(cartid=c_id(request))    #else create a cart id
        ct.save()
    try:
        c_items=items.objects.get(prod=prod,cart=ct)          #if product is exist
        if c_items.quan < c_items.prod.stock:
            c_items.quan += 1
        c_items.save()
    except items.DoesNotExist:                               #add product
        c_items=items.objects.create(prod=prod,quan=1,cart=ct)
        c_items.save()


    return redirect('cart_details')


def cart_details(request, tot=0, count=0, ct_items=None):
    
    try:
        ct = cart.objects.get(cartid=c_id(request))

        ct_items = items.objects.filter(cart=ct, active=True)
        for i in ct_items:
            tot += (i.prod.price * i.quan)
            count += i.quan
    except ObjectDoesNotExist:
        return HttpResponse("<script>alert('empty cart');window.location.href='/';</script>")
    return render(request, 'cart.html', {"ci": ct_items, 't': tot, 'cn': count})







def increment_item(request, item_id):
    item = get_object_or_404(items, id=item_id)
    if item.quan < item.prod.stock:
        item.quan += 1
        item.save()
    return redirect('cart_details')

def decrement_item(request, item_id):
    item = get_object_or_404(items, id=item_id)
    if item.quan > 1:
        item.quan -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart_details')



def delete_item(request, item_id):
    item = get_object_or_404(items, id=item_id)
    item.delete()
    return redirect('cart_details')




