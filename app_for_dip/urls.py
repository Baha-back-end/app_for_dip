from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', category_page_view, name='category'),
    path('about_us/', about_us_page_view, name='about_us'),
    path('contact_with_us/', contact_with_us_page_view, name='contact_with_us'),
    path('shops/', shops_page_view, name='shops'),
    path('product/<int:product_id>/', product_detail_page_view, name='product_detail'),
    path('add_product/', add_product_view, name='add_product'),
    path('user_register/', user_register_view, name="register"),
    path('user_login/', user_login_view, name="login"),
    path('user_logout/', logout_user_view, name="logout"),
    path('update_product/<int:product_id>/', update_product_view, name='update_product'),
    path('delete_product/<int:product_id>/', delete_product_view, name="delete_product"),
    path('search/', search_view, name="search")
]