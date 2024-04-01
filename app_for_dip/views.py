from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .models import *
from .forms import *



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


def product_detail_page_view(request, product_id):
    product = Product.objects.get(id=product_id)
    new_products = Product.objects.all().order_by('-added_at')[:8]

    context = {
        "title": f"Товар: {product.title}",
        "product": product,
        "new_products": new_products,

    }
    return render(request, 'product_detail.html', context)


def add_product_view(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        form = ProductForm()

        context = {
            "title": "Добавить товар",
            "form": form
        }
        return render(request, 'add_product.html', context)


def user_register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            return redirect('login')
        else:
            # TODO: ERROR MESSAGE
            pass
    else:
        form = UserRegistrationForm()
    context = {
        "title": "Регистрация пользователья",
        "form": form
    }
    return render(request, "register.html", context)


def user_login_view(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('index')
            else:
                # TODO: ERROR MESSAGE
                pass
        else:
            # TODO: ERROR MESSAGE
            pass
    else:
        form = UserLoginForm()
    context = {
        "title": "Войти в аккаунт",
        "form": form
    }
    return render(request, "login.html", context)


def logout_user_view(request):
    logout(request)
    return redirect('index')


def update_product_view(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        form = ProductForm(instance=product,
                           data=request.POST,
                           files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_detail", product_id)
        else:
            # TODO: ERROR MESSAGE
            return redirect("update_product", product_id)
    else:
        form = ProductForm(instance=product)

    context = {
        "form": form,
        "title": "Обновить товар"
    }
    return render(request, "add_product.html", context)


def delete_product_view(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == "POST":
        product.delete()
        return redirect("index")

    context = {
        "title": "Удаление товара",
        "product": product
    }

    return render(request, "delete.html", context)


def search_view(request):
    word = request.GET.get("q")
    categories = Category.objects.all()
    producs = Product.objects.filter(
        title__iregex=word
    )
    context = {
        "products": producs,
        "categories": categories,
        "title": "Результаты поиска"

    }

    return render(request, "main_page.html", context)


def profile_page_view(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)

    context = {
        "profile": profile,
        "title": "Мой профиль"
    }

    return render(request, "profile.html", context)


def edit_profile_view(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)

    if request.method == "POST":
        user_form = UserForm(instance=user, data=request.POST)
        profile_form = ProfileForm(instance=profile, data=request.POST,
                                   files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile", user.id)
        else:
            # TODO: ERROR MESSAGE
            return redirect("edit_profile.html", user.id)
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "title": "Изменить профиль"
    }
    return render(request, "edit_profile.html", context)

