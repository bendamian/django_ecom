from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404



from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


# Create your views here.
# API view to return the latest 4 products


class LatestProductsList(APIView):
    def get(self, request, format=None):
        # Fetch the most recent 4 products (you could order explicitly)
        limit = int(request.query_params.get('limit', 4))  # Default to 4
        products = Product.objects.all().order_by('-date_added')[:limit]
        # products = Product.objects.all().order_by('-date_added')[:4]
      
        # Serialize the queryset into JSON
        serializer = ProductSerializer(products, many=True)

        # Return serialized data as a JSON response
        return Response(serializer.data)


# API view to retrieve a single Category by its slug
class CategoryDetailView(APIView):
    def get(self, request, slug, format=None):
        # Try to get the category by slug or return 404 if not found
        category = get_object_or_404(Category, slug=slug)

        # Serialize the category object into JSON
        serializer = CategorySerializer(category)

        # Return the serialized data with a 200 OK response
        return Response(serializer.data, status=status.HTTP_200_OK)


# API view to retrieve a single Product by category and product slug
class ProductDetailView(APIView):
    def get(self, request, category_slug, product_slug, format=None):
        # Look up the product by its slug and its related category's slug
        # Raises 404 if not found
        product = get_object_or_404(
            Product,
            slug=product_slug,
            category__slug=category_slug
        )

        # Serialize the product into JSON format
        serializer = ProductSerializer(product)

        # Return serialized product data with HTTP 200 OK status
        return Response(serializer.data)
