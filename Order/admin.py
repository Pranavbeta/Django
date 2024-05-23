from django.contrib import admin

# Register your models here.
from Order.models import Order,Order_detail
# Register your models here.
admin.site.register(Order)
admin.site.register(Order_detail)