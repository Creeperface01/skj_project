from django.urls import path

from eshop.views import auth, cart, product, user

urlpatterns = [
    path('orders', user.orders, name='orders'),
    path('profile', user.profile, name='profile'),
    path('category/<category>', product.default, name='default'),
    path('cart/checkout', cart.checkout, name='cart_checkout'),
    path('cart/address', cart.address, name='cart_address'),
    path('cart/shipping', cart.shipping, name='cart_shipping'),
    path('cart/payment', cart.payment, name='cart_payment'),
    path('cart/summary', cart.summary, name='cart_summary'),
    path('cart/complete', cart.complete, name='cart_complete'),
    path('login', auth.login, name='login'),
    path('register', auth.register, name='register'),
    path('logout', auth.logout, name='logout'),
    path('<slug>', product.show, name='product_show'),
]
