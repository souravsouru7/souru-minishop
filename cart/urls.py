from django.urls import path
from.import views


urlpatterns = [
    # ...
    path('cart_details',views.cart_details, name='cart_details'),
    path("add/<int:product_id>/",views.add_cart,name='addcart'),
    path('increment_item/<int:item_id>/', views.increment_item, name='increment_item'),
    path('decrement_item/<int:item_id>/', views.decrement_item, name='decrement_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    
    path("bank",views.bank_form,name="bank"),
    path("checkout",views.billing_form,name="checkout"),
    path('success', views.success, name='success'),
    path("pay",views.pay,name="pay"),
]
