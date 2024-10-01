from django.urls import path
from . import views

urlpatterns = [
    # path('shop2',views.shop2,name='shop2'),
    # path('',views.index,name='index'),
    # path('combine',views.combine,name='combine'),
    path('', views.index, name='index'),
]
