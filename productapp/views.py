from django.shortcuts import render, redirect

from .forms import ProductForm
from .models import Product
# # from django. http import HttpResponse

# Create your views here.
def index(request):
    product=Product.objects.all()
    context={
        'product_list':product
    }
    return render(request,'index.html', context)

def detail(request, product_id):
    product=Product.objects.get(id=product_id)
    return render(request,"detail.html",{'product':product})

def add_product(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        price=request.POST.get('price',)
        img=request.FILES['img']
        product=Product(name=name,desc=desc,price=price,img=img)
        product.save()
    return render(request, 'add.html')


def update(request, id):
    product=Product.objects.get(id=id)
    form=ProductForm(request.POST or None, request.FILES, instance=product)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form':form, 'product':product})


def delete(request, id):
    if request.method=='POST':
        product=Product.objects.get(id=id)
        product.delete()
        return redirect('/')
    return render(request,'delete.html')







