from django.urls import path,re_path

from . import views

app_name = 'cart'

urlpatterns = [
    re_path(r'^$', views.cart_detail, name='cart_detail'),
    re_path(r'^add/(?P<id>\d+)/$', views.cart_add, name='cart_add'),
]