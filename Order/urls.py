from django.urls import path   # type: ignore
from Order import views
from Product import urls
urlpatterns = [
    path('',views.home,name='home'),
    path('order/', views.order, name='order'),
    path('new_order/',views.new_order,name='new_order'),
   # path('manage/', views.Dashboard, name='manage'),
]