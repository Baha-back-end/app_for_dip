from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True,
                             verbose_name= "Название категории")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Product(models.Model):
    title = models.CharField(max_length=255, unique=True,
                             verbose_name= "Наименование товара")
    description = models.TextField(verbose_name= "Описание товара")
    image = models.ImageField(upload_to="products/",
                              null=True, blank=True,
                              verbose_name= "Фото товара")
    parameters = models.TextField(default='', null=True,
                                  verbose_name= "Характеристики товара")
    price = models.FloatField(max_length=12, null=True,
                              verbose_name= "Цена товара")
    reviews = models.IntegerField(default=0, verbose_name= "Просмотры")
    added_at = models.DateTimeField(auto_now_add=True, verbose_name= "Дата добавление товара")
    updated_at = models.DateTimeField(auto_now=True, verbose_name= "Дата обновление товара")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name= "Категория товара")
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name= "Кто добавил товар")


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Contact_with_us(models.Model):
    full_name = models.CharField(max_length=255, verbose_name= "Имя фамилия")
    expert = models.CharField(max_length=255, verbose_name= "Направления эксперта")
    photo = models.ImageField(upload_to="experts/", verbose_name= "Фото эксперта")
    phone_number = models.TextField(max_length=15)
    telegram = models.URLField(validators=[
        RegexValidator(r'^https?:\/\/t\.me\/[a-zA-Z0-9_-]{5,}$')
    ], verbose_name= "Телеграмм")
    instagram = models.URLField(validators=[
        RegexValidator(r'^https?:\/\/www\.instagram\.com\/[a-zA-Z0-9_-]{5,}$')
    ], verbose_name= "Инстаграм")
    facebook = models.URLField(validators=[
        RegexValidator(r'^https?:\/\/www\.facebook\.com\/[a-zA-Z0-9_-]{5,}$')
    ], verbose_name= "Фейсбук")
    vkontakte = models.URLField(validators=[
        RegexValidator(r'^https?:\/\/vk\.com\/[a-zA-Z0-9_-]{5,}$')
    ], verbose_name= "Вконтакте")

    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = "Эксперт"
        verbose_name_plural = "Эксперты"

class Profile(models.Model):
    phone = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="********",
        verbose_name= "Телефон номер"
    )
    mobile = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="********",
        verbose_name="Мобильный номер"
    )
    address = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="********",
        verbose_name="Адрес"
    )
    job = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="********",
        verbose_name="Профессия"
    )
    image = models.ImageField(upload_to=' profiles/', null=True, blank=True, verbose_name= "Фото")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name= "Пользователь")

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= "Автор")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name= "Товар")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name= "Добавлено")
    text = models.TextField(verbose_name="Отзыв:")

    def __str__(self):
        return self.author.username
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"









