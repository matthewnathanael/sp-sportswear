from django.urls import path
from main.views import show_main, create_product, show_products, show_xml, show_json,show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_product,delete_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('product/create/', create_product, name='create_product'),
    path('product/<str:id>/', show_products, name='show_products'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<int:id>/edit', edit_product, name='edit_product'),
    path('product/<int:id>/delete', delete_product, name='delete_product'),
]