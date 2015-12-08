from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Avg
from .models import Product, ProductRating, ProductReview

def index(request):
	products = Product.objects.all()
	for p in products:
		ratings = ProductRating.objects.all().filter(product=p)
		p.avgRating = ratings.aggregate(Avg('rating')).get("rating__avg", 0)
		p.ratingCount = len(ratings)
		p.productJSON = p.jsonValue(request)

	return render(request, 'index.html', {"products": products})

def product(request, productID):
	product = Product.objects.get(id=productID)
	ratings = ProductRating.objects.all().filter(product=product)
	reviews = ProductReview.objects.all().filter(product=product)
	avgRating = ratings.aggregate(Avg('rating'))
	avgRating = avgRating.get("rating__avg", 0)
	return render(request, 'product.html', {"product": product, "productJSON":product.jsonValue(request), "averageRating": avgRating, "ratingCount":len(ratings), "reviews":reviews})