from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'parameters', 'price', 'reviews', 'added_at', 'updated_at')
    list_filter = ('category', 'added_at')
    readonly_fields = ('reviews',)


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Profile)
admin.site.register(Contact_with_us)


