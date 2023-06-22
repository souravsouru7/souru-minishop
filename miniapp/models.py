from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.
class cate(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])
    def __str__(self):
        return self.name
    
class product(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(cate,on_delete=models.CASCADE)
    date=models.DateField()
    
    def __str__(self):
        return self.name
    
  
    def get_url(self):
        return reverse('detail',args=[self.category.slug,self.slug])\
        

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