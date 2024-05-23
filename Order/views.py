from django.shortcuts import render,redirect
from datetime import datetime
from Product.models import Product
from Order.models import Order,Order_detail
from decimal import Decimal
# Create your views here.


def new_order(request):
    if request.method == 'POST':
        name = request.POST.get('customerName')
        product_id = int( request.POST.get('Product'))
        quantity = request.POST.get("quantity[]")
        total =Decimal(request.POST.get("total[]","0"))
        grand_total=Decimal(request.POST.get("total","0"))
        #order_id =int(request.POST.get('customerName'))
        # First, save the order
        Orders = Order(customer_name=name, total_cost=grand_total, date=datetime.today())
        Orders.save()

        # Save the order detail
        product_instance = Product.objects.get(id=product_id)
        Details = Order_detail(order_id=Orders,quantity=quantity, total_price=total, product_id=product_instance)
        Details.save()
        return redirect('order')
    else:
        Products = Product.objects.all()
        return render(request,"order.html",{'Products':Products})
    

def order(request):
    orders=Order.objects.all()
    return render(request,"order_history.html",{'Orders':orders})

def manage(request):
    return render(request,"manage.html")

def home(request):
    return render(request,"home.html")