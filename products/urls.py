from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='Home'),
    path('store_new_product/',views.store_product,name='Storeproduct'),
    path('show_product/',views.show_product,name='Showproduct'),
    path('edit_product/<int:id>',views.edit_product,name='Editproduct'),
    path('delete_product/<int:id>',views.delete_product,name='Deleteproduct'),
]
