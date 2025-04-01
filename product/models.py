from django.db import models
from django.utils.text import slugify
from django.urls import reverse  # better practice for URL resolution
from PIL import Image
from io import BytesIO
from django.core.files import File


# Create your models here.


class Category(models.Model):
    # Name of the category (e.g., "Science", "Technology", etc.)
    name = models.CharField(max_length=255)

    # URL-friendly version of the category name, must be unique for reverse URL lookups
    # blank=True allows slug to be empty before saving
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        # Sort categories alphabetically by name
        ordering = ('name',)
        verbose_name_plural = "categories"  # Optional: improves admin display

    def __str__(self):
        # Display the category name in human-readable contexts (e.g., admin site)
        return self.name

    def get_absolute_url(self):
        # Returns the canonical URL for this category
        # It's better to use reverse() for future flexibility
        return reverse('product:category_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        # Auto-generate slug from name if it's not set
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Product(models.Model):
    # Link to the Category this product belongs to
    category = models.ForeignKey(
        'Category',
        related_name='products',
        on_delete=models.CASCADE
    )

    # Product name
    name = models.CharField(max_length=255)

    # URL-friendly slug (can be auto-generated if needed)
    slug = models.SlugField(unique=True, blank=True)  # allow auto-generation

    # Optional description of the product
    description = models.TextField(blank=True, null=True)

    # Price with up to 6 digits total and 2 decimal places
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # Main product image (optional)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    # Thumbnail image (optional, can be auto-generated from image)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    # Timestamp when the product was added
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Newest products appear first by default
        ordering = ('-date_added',)

    def __str__(self):
        # String representation of the product
        return self.name

    def get_absolute_url(self):
        # Generates the product's URL using category and product slug
        return reverse('product:product_detail', kwargs={
            'category_slug': self.category.slug,
            'product_slug': self.slug
        })

    def get_image(self):
        # Returns full image URL if it exists
        if self.image:
            return f'http://127.0.0.1:8000{self.image.url}'
        return ''

    def get_thumbnail(self):
        # Returns full thumbnail URL if it exists; generates one if it doesn't
        if self.thumbnail:
            return f'http://127.0.0.1:8000{self.thumbnail.url}'
        elif self.image:
            self.thumbnail = self.make_thumbnail(self.image)
            self.save()
            return f'http://127.0.0.1:8000{self.thumbnail.url}'
        return ''

    def make_thumbnail(self, image, size=(300, 200)):
        # Generates a thumbnail from the original image
        img = Image.open(image)
        img = img.convert('RGB')  # Ensure image is in RGB mode
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail

    def save(self, *args, **kwargs):
        # Auto-generate slug from name if it's not already set
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

