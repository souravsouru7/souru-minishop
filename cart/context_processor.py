from miniapp.models import *
from .models import items,cart
from django.core.exceptions import ObjectDoesNotExist
def catey(request):
    catayy=cate.objects.all()
    return {"cata":catayy}


def cart_quantity(request):
    if request.user.is_authenticated:
        try:
            ct = cart.objects.get(cartid=c_id(request))
            count = items.objects.filter(cart=ct, active=True).count()
            return {'cart_quantity': count}
        except ObjectDoesNotExist:
            pass
    return {'cart_quantity': 0}
