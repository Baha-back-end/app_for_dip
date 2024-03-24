from django.shortcuts import render

from .models import *


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        "title": "Главная страница",
        "categories": categories,
        "products": products
    }

    return render(request, "main_page.html", context)


def category_page_view(request, category_id):
    products = Product.objects.filter(category=category_id)
    hot_products = Product.objects.all().order_by('-reviews')

    context = {
        "title": f"Категория: {Category.objects.get(id=category_id).title}",
        "products": products,
        "hot_products": hot_products
    }

    return render(request, "category_page.html", context)


def about_us_page_view(request):
    context = {
        "title": "О нас"
    }

    return render(request, "about_us.html", context)

def contact_with_us_page_view(request):
    context = {
        "title": "Связаться с нами"
    }

    return render(request, "contact_with_us.html", context)


def shops_page_view(request):
    context = {
        "title": "Магазыны"
    }

    return render(request, "shops.html", context)



def product_parameters_page_view(request, product_id):
    product = Product.objects.get(id=product_id)
    new_products = Product.objects.all().order_by('-added_at')[:3]

    context = {
        "title": f"Товар: {product.title}",
        "product": product,
        "new_products": new_products,

    }
    return render(request, 'product_parameters.html', context)








