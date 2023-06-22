from django.urls import path
from.import views
urlpatterns = [
    path('',views.home,name='index'),
    path('about',views.about,name="about"),
    path('blog-single',views.blogsingle,name="blog-single"),
    path('blog',views.blog,name="blog"),
    path("checkout",views.billing_form,name="checkout"),
    path('contact',views.contact,name="contact"),
    
    path('shop',views.shop,name="shop"),
    path("bank",views.bank_form,name="bank"),
    
   
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('<str:c_slug>/<str:product_slug>/', views.detail, name='detail'),
    path('search',views.search,name='search'),
    path('register', views.register,name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout_view, name='logout'),

]
