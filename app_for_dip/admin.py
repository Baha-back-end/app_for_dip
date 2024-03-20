from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'parameters', 'price', 'reviews', 'added_at', 'updated_at')
    list_filter = ('category', 'added_at')
    readonly_fields = ('revews',)


admin.site.register(Category)
admin.site.register(Product, ArticleAdmin)


