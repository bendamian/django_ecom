from rest_framework import serializers
from .models import Category, Product

# Serializer for the Category model


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'get_absolute_url']
        read_only_fields = ['slug', 'get_absolute_url']


# Serializer for the Product model
class ProductSerializer(serializers.ModelSerializer):
    # Nested category details (optional)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'name', 'slug', 'description',
            'price', 'image', 'thumbnail', 'get_image',
            'get_thumbnail', 'get_absolute_url', 'date_added'
        ]
        read_only_fields = [
            'slug', 'get_image', 'get_thumbnail',
            'get_absolute_url', 'thumbnail', 'date_added'
        ]
