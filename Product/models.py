from django.db import models


# Create your models here.
class uom(models.Model):
    uom_name=models.CharField(max_length=122)
    
    class Meta:
        db_table='uom'

    
class Product(models.Model):
    name=models.CharField(max_length=122)
    uom=models.ForeignKey(uom,on_delete=models.SET_NULL,null=True)
    price_per_unit=models.BigIntegerField()

    class Meta:
        db_table='Product'
