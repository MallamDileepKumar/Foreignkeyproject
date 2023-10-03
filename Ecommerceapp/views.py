from django.shortcuts import render
from .models import Category,Product
# Create your views here.
def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    print(products)
    return render(request,'index.html',{'categories':categories,'products':products},)

def category(request,name):
    categories = Category.objects.get(name=name)
    products = Product.objects.filter(Category=categories)
    return render(request, 'category.html', {'categories': categories, 'products': products}, )
