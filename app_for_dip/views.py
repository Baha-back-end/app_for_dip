from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
    comments = Comment.objects.filter(product=product_id)
    if request.user.id != product.author.id:
        product.reviews += 1
        product.save()

    context = {
        "title": f"Товар: {product.title}",
        "product": product,
        "new_products": new_products,
        "comments": comments
    }
    if request.user.is_authenticated:
        context.update({
            "form": CommentForm()
        })

    return render(request, 'product_detail.html', context)


@login_required(login_url="login")
def add_product_view(request):
    if request.method == "POST":
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            messages.success(request, "Товар добавлен успешно !")
            return redirect("product_detail", product.id)
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect("add_product")

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
            profile.save()
            messages.success(request, "Профиль создано успешно")
            return redirect('login')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect('register')
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
                messages.success(request, "Вы вошли в аккаунт !")
                return redirect('index')
            else:
                messages.error(request, "Логин или пароль введен не верно!")
                return redirect('login')
        else:
            messages.error(request, "Логин или пароль введен не верно!")
            return redirect('login')
    else:
        form = UserLoginForm()
    context = {
        "title": "Войти в аккаунт",
        "form": form
    }
    return render(request, "login.html", context)

@login_required(login_url="login")
def logout_user_view(request):
    logout(request)
    messages.info(request, "Вы вышли с аккаунта!")
    return redirect('index')

@login_required(login_url="login")
def update_product_view(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        form = ProductForm(instance=product,
                           data=request.POST,
                           files=request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Товар успешно обновлен!")
            return redirect("product_detail", product_id)
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect("update_product", product_id)
    else:
        form = ProductForm(instance=product)

    context = {
        "form": form,
        "title": "Обновить товар"
    }
    return render(request, "add_product.html", context)

@login_required(login_url="login")
def delete_product_view(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == "POST":
        product.delete()
        messages.warning(request, "Товар удален!")
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
    messages.info(request, "Результаты поиска!")
    return render(request, "main_page.html", context)

@login_required(login_url="login")
def profile_page_view(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)

    context = {
        "profile": profile,
        "title": "Мой профиль"
    }

    return render(request, "profile.html", context)

@login_required(login_url="login")
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
            messages.success(request, "Данные профиля успешно обновлены!")
            return redirect("profile", user.id)
        else:
            for field in user_form.errors:
                messages.error(request, user_form.errors[field].as_text())
            for field in profile_form:
                messages.error(request, profile_form.errors[field].as_text())

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

@login_required(login_url="login")
def save_comment(request, product_id):
    product = Product.objects.get(id=product_id)
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.product = product
        comment.author = request.user
        comment.save()
        messages.success(request, "Отзыв добавлен успешно!")
        return redirect('product_detail', product_id)
