from django.contrib import admin
from .models import cart,items,BankDetails,BillingDetails
admin.site.register(cart)
admin.site.register(items)
admin.site.register(BankDetails)
admin.site.register(BillingDetails)

