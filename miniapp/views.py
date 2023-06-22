from django.shortcuts import render,get_object_or_404,redirect
from .models import product,cate
from django.http import HttpResponse 
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login  as auth_login
from django.contrib.auth import logout
from django.contrib.auth.models import User,auth
from django.contrib import messages

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
    
def register(request):
    if request.method == "POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        email=request.POST["email"]

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is already taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is already taken")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("user created")
        else:
            print("passwored is not correct")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,"register.html")



def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid details")
            return redirect("login")
        
    else:
        return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect('/')