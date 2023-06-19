from django.urls import path
from.import views
urlpatterns = [
    path('',views.home,name='index'),
    path('about',views.about,name="about"),
    path('blog-single',views.blogsingle,name="blog-single"),
    path('blog',views.blog,name="blog"),
    path("checkout",views.checkout,name="checkout"),
    path('contact',views.contact,name="contact"),
    
    path('shop',views.shop,name="shop"),
    
   
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('<str:c_slug>/<str:product_slug>/', views.detail, name='detail'),
    path('search',views.search,name='search')
]
