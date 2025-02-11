from django.urls import path
from . import views

urlpatterns = [

    path('', views.product_list, name='product-list'),
    path('create/', views.create_product, name='create-product'),
    path('edit/<int:pk>/', views.edit_product, name='edit-product'),
    path('delete/<int:pk>/', views.delete_product, name='delete-product'),
    path('api/edit/<int:pk>',views.update_product,name='update_product'),
    path('api/delete/<int:pk>',views.delete_blog_post,name='delete_blog_post'),
    

]
