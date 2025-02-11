from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

# API Views
@api_view(['GET'])
def dbdata(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_blog_post(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Blog post created successfully'}, status=201)
    return render(request, 'create-product.html')

@api_view(['PUT'])
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_blog_post(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return Response({'message': 'Blog post deleted successfully'}, status=status.HTTP_200_OK)

# Template-Based Views
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product-list.html', {'products': products})

def create_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        Product.objects.create(title=title, content=content, author=author)
        return redirect('product-list')
    return render(request, 'create-product.html')

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.title = request.POST.get('title')
        product.content = request.POST.get('content')
        product.author = request.POST.get('author')
        product.save()
        return redirect('product-list')
    return render(request, 'edit-product.html', {'product': product})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product-list')
