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

    return render(request, "index.html", context)
