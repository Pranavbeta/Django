from django.db import models
from Product.models import Product,uom
# Create your models here.
class Order(models.Model):
    customer_name=models.CharField(max_length=122)
    total_cost=models.BigIntegerField()
    date=models.DateField()
    class Meta:
        db_table='Order'

class Order_detail(models.Model):
    order_id=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    product_id=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity=models.DecimalField(max_digits=6,decimal_places=3)
    total_price=models.BigIntegerField()
    class Meta:
        db_table='Order_detail'

