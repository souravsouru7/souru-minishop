from django.shortcuts import render,get_object_or_404
from .models import product,cate
from django.http import HttpResponse 
from django.core.paginator import Paginator

# Create your views here.

def home(request,c_slug=None):
    pagi=product.objects.order_by('id')
    paginator=Paginator(pagi,5)
    page=request.GET.get('page')
    paginated=paginator.get_page(page)

        
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(cate,slug=c_slug)
        prodt=product.objects.filter(category=c_page,available=True)
    else:
        prodt=product.objects.all().filter(available=True)
    catayy=cate.objects.all()
    
    

    return render(request,'index.html',{"prodt":prodt,"cata":catayy,"paginated":paginated})
def about(request):
    return render(request,'about.html')
def blogsingle(request):
    return render(request,'blog-single.html')
def blog(request):
    return render(request,'blog.html')

def checkout(request):
    return render(request,"checkout.html")
def contact(request):
    return render(request,"contact.html")
def productsingle(request):
    return render(request,"")
def shop(request):
    return render(request,'shop.html')



def detail(request, c_slug, product_slug):
    prodt = get_object_or_404(product, category__slug=c_slug, slug=product_slug)
    return render(request, "product-single.html", {'prodt': prodt})


def search(request):
    
    sea=request.GET.get('sea')
    result=product.objects.filter(name__icontains=sea)if sea else []
    return render(request,'search.html',{"result":result})
    


    