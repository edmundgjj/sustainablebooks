from django.urls import path
from .views import add_to_cart, view_cart, remove_from_cart, update_quantity


urlpatterns = [
    path('add/<book_id>', add_to_cart, name='add_to_cart'),
    path('', view_cart, name='view_cart'),
    path('remove/<book_id>', remove_from_cart, name='remove_from_cart'),
    path('update_quantity/<book_id>', update_quantity,
         name='update_cart_quantity_route')
]
