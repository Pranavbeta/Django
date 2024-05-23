from django.shortcuts import render,redirect
from django.http import HttpResponse
from Product.models import Product,uom

def Dashboard(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        uom_id = int( request.POST.get('uoms'))
        price = request.POST.get('price')
        
        uom_instance = uom.objects.get(id = uom_id)

        Products=Product(name = name,uom = uom_instance, price_per_unit = price)

        Products.save()
        return redirect('manage')
    else:
        uoms = uom.objects.all()
        Products = Product.objects.all()
        return render(request,"manage.html",{'uoms':uoms,'Products':Products})
    #return render(request,"manage.html",{'Products':Products})

     

# Create your views here.
def delete(request, Id):
    Products = Product.objects.get( id = Id)
    Products.delete()
    return redirect('manage') 