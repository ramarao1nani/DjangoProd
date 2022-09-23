from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return HttpResponse("hello There")

def products(request):
    page_obj = listOfProducts=Product.objects.all()
    product_name=request.GET.get('product_name')
    if(product_name!='' and product_name is not None):
        page_obj=listOfProducts.filter(name__icontains=product_name)
    paginator=Paginator(page_obj,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={
        'page_obj' : page_obj
    }
    return render(request,'myapp/index.html',context)

class ProductListView(ListView):
    model=Product
    template_name='myapp/index.html'
    context_object_name='products'

def product_detail(request,id):
    detailedProduct=Product.objects.get(id=id)
    context={
        'product' : detailedProduct
    }
    return render(request,'myapp/detail.html',context)

class ProductDetailView(DetailView):
    model=Product 
    template_name='myapp/detail.html'
    context='product'

@login_required
def add_product(request):
    if(request.method=='POST'):
        name=request.POST.get('name')
        price=request.POST.get('price')
        desc=request.POST.get('desc')
        image=request.FILES['upload']
        seller_name=request.user
        product = Product(name=name,price=price,desc=desc,image=image,seller_name=seller_name)
        product.save()
    return render(request,'myapp/addproduct.html')

def update_product(request,id):
    product=Product.objects.get(id=id)
    if(request.method=='POST'):
        product.name  =  request.POST.get('name')
        product.price =  request.POST.get('price')
        product.desc  =  request.POST.get('desc')
        if(request.FILES.get('upload')):
            product.image =  request.FILES['upload']
        product.save()
        return redirect('/myapp/products')
    context={
        'product': product
    }
    return render(request,'myapp/updateproduct.html',context)

def delete_product(request,id):
    product=Product.objects.get(id=id)
    context={
        'product':product 
    } 
    if(request.method=='POST'):
        product.delete()
        return redirect('/myapp/products')
    return render(request,'myapp/deleteproduct.html',context)

def my_listings(request):
    product = Product.objects.filter(seller_name=request.user)
    context = {'products': product}
    return render(request, 'myapp/mylistings.html', context)