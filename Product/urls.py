from django.urls import path   # type: ignore
from Product import views

urlpatterns = [
    path('manage/', views.Dashboard, name='manage'),
    path('delete/<int:Id>',views.delete,name='delete')
]