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
    reviews = models.TextField(default='', null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title




