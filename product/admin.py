from django.contrib import admin
from .models import Category, Product

# Optional: Customize Category admin display


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Show these fields in the category list view
    list_display = ('name', 'slug')
    # Automatically fill slug based on the name in the admin form
    prepopulated_fields = {'slug': ('name',)}
    # Add a search bar for categories
    search_fields = ('name',)
    # Ordering in admin
    ordering = ('name',)

# Optional: Customize Product admin display


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Show these fields in the product list view
    list_display = ('name', 'category', 'price', 'date_added')
    # Filters in the sidebar
    list_filter = ('category', 'date_added')
    # Add a search bar
    search_fields = ('name', 'description')
    # Automatically fill slug based on the name
    prepopulated_fields = {'slug': ('name',)}
    # Field ordering in the form (optional)
    ordering = ('-date_added',)
