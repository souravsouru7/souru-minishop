from django.db import models
from miniapp.models import product
from django.contrib.auth.models import User





class cart(models.Model):
    cartid=models.CharField(max_length=1000,unique=True)
    date=models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None,null=True)
    


class items(models.Model):
    prod=models.ForeignKey(product,on_delete=models.CASCADE)    #here class/tale product from shop is act as a foreign key so we can fetch the values ...
    cart=models.ForeignKey(cart,on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)

    
    def total(self):
        return self.prod.price*self.quan


class BillingDetails(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class BankDetails(models.Model):
    billing_details = models.OneToOneField(BillingDetails, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=50)
    account_holder_name = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)

    def __str__(self):
        return self.account_number