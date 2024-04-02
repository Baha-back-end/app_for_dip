from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="products/",
                              null=True, blank=True)
    parameters = models.TextField(default='', null=True)
    price = models.FloatField(max_length=12, null=True)
    reviews = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title



class Contact_with_us(models.Model):
    full_name = models.CharField(max_length=255)
    expert = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="experts/")
    phone_number = models.TextField(max_length=15)
    telegram = models.URLField(validators=[
        RegexValidator(r'^https?:\/\/t\.me\/[a-zA-Z0-9_-]{5,}$')
    ])
    instagram = models.URLField(validators=[
        RegexValidator(r'^https?:\/\/www\.instagram\.com\/[a-zA-Z0-9_-]{5,}$')
    ])
    facebook = models.URLField(validators=[
        RegexValidator(r'^https?:\/\/www\.facebook\.com\/[a-zA-Z0-9_-]{5,}$')
    ])
    vkontakte = models.URLField(validators=[
        RegexValidator(r'^https?:\/\/vk\.com\/[a-zA-Z0-9_-]{5,}$')
    ])

    def __str__(self):
        return self.full_name


class Profile(models.Model):
    phone = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="********"
    )
    mobile = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="********")
    address = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="********")
    job = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="********")
    image = models.ImageField(upload_to=' profiles/', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    porduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.author










