from django.shortcuts import render, get_object_or_404
from .models import Product, Category

from .forms import ProductModelForm
from django.http import HttpResponse


# Create your views here.
def home(request, slug_c=None):
    page_c = None
    products = None
    if slug_c != None:
        page_c = get_object_or_404(Category, slug=slug_c)
        products = Product.objects.all().filter(category=page_c, available=True)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request, 'home.html', {'category': page_c, 'products': products})


def product_details(request, slug_c, slug_p):
    try:
        product = Product.objects.get(category__slug=slug_c, slug=slug_p)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})


def cart(request):
    return render(request, 'cart.html')


def book_register(request):
    if request.method == 'POST':

        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("successfully registered product")
    form = ProductModelForm()
    return render(request, 'book_register.html', {'form': form})
