from django.contrib import admin

from .models import Product, ProductReview, ProductRating

admin.site.register(Product)
admin.site.register(ProductReview)
admin.site.register(ProductRating)