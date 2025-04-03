from django.urls import path
from . import views

# This gives your app a URL namespace
app_name = 'product'
urlpatterns = [
    path('products/<slug:category_slug>/<slug:product_slug>/',
         views.ProductDetailView.as_view(), name='product_detail'),
    path('latest-products/', views.LatestProductsList.as_view(),
         name='latest_products'),
    path('category/<slug:slug>/',
         views.CategoryDetailView.as_view(), name='category_detail'),
]
