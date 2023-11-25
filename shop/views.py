from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        # language = request.LANGUAGE_CODE
        category = get_object_or_404(
            Category,
            # translations__language_code=language,
            slug=category_slug
        )
        products = Product.objects.filter(category=category)

    context = {'category': category,
               'categories': categories, 'products': products}
    return render(request, 'shop/product/list.html', context)


def product_detail(request, pk, slug):
    # language = request.LANGUAGE_CODE
    product = get_object_or_404(
        Product,
        id=pk,
        slug=slug,
        available=True
    )
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, 'shop/product/detail.html', context)
