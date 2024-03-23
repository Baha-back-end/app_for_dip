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


