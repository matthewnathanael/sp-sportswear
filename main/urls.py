from django.urls import path
from main.views import show_main, create_product, show_products, show_xml, show_json,show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_product,delete_product,add_product_entry_ajax,delete_product_ajax, edit_product_entry_ajax,register_ajax,login_ajax,proxy_image,create_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('product/create/', create_product, name='create_product'),
    path('product/<uuid:id>/', show_products, name='show_products'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('create-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('product/<uuid:id>/edit-ajax/', edit_product_entry_ajax, name='edit_product_entry_ajax'),
    path('product/<uuid:id>/delete-ajax/', delete_product_ajax, name='delete_product_ajax'),
    path('register-ajax/', register_ajax, name='register_ajax'), 
    path('login-ajax/', login_ajax, name='login_ajax'),         
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]