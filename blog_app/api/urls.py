from django.urls import path
from product.views import dbdata
from product import views

urlpatterns = [
    path('create-blog/', views.create_blog_post, name='create-blog-post'),
    path('delete-blog/<int:pk>/', views.delete_blog_post, name='delete-blog-post'),
    path('dbdata/', dbdata)
]