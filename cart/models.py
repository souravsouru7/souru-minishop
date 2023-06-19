from django.db import models
from miniapp.models import product





class cart(models.Model):
    cartid=models.CharField(max_length=1000,unique=True)
    date=models.DateField(auto_now_add=True)


class items(models.Model):
    prod=models.ForeignKey(product,on_delete=models.CASCADE)    #here class/tale product from shop is act as a foreign key so we can fetch the values ...
    cart=models.ForeignKey(cart,on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)

    
    def total(self):
        return self.prod.price*self.quan


