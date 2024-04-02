from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'parameters', 'price', 'reviews', 'added_at', 'updated_at')
    list_filter = ('category', 'added_at')
    readonly_fields = ('reviews', 'author')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user

        super(ProductAdmin, self).save_model(
            request, obj, form, change
        )


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Profile)
admin.site.register(Contact_with_us)


