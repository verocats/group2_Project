from django.shortcuts import render, get_object_or_404
from django.apps import apps
order = apps.get_model('orders', 'Order')
from .models import Category, Product
from django.db.models import Q
from cart.forms import CartAddProductForm

def product_list(request, category_slug=None):
    category = None
    search_term = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    if 'search' in request.GET:
        search_term = request.GET['search']
        products = Product.objects.filter(available=True)
        products = products.filter(Q(description__icontains=search_term) | Q(name__icontains=search_term) | Q(category__name__icontains=search_term)).distinct()

    return render(request,
                  'productlist.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'searchterm': search_term})


def product_detail(request, id, slug):
    category = None
    search_term = None
    categories = Category.objects.all()
    if 'search' in request.GET:
        search_term = request.GET['search']
        products = Product.objects.filter(available=True)
        products = products.filter(Q(description__icontains=search_term) | Q(name__icontains=search_term) | Q(category__name__icontains=search_term)).distinct()
        return render(request,
                      'productlist.html',
                      {'category': category,
                       'categories': categories,
                       'products': products,
                       'searchterm': search_term})

    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'productdetail.html', {'product': product,'cart_product_form': cart_product_form})



