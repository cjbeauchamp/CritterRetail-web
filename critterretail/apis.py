from django.http import JsonResponse, HttpResponse
from .models import Product, ProductRating
from django.db.models import Avg
from random import randint
import time
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Product, ProductReview

def confirmPayment(request, code):
	time.sleep(randint(2,8))
	print code
	codes = [200, 300, 500, 600]
	if int(code) not in codes:
		code = 400
	return HttpResponse(status=code)

def completePurchase(request):
	time.sleep(randint(2,8))
	return HttpResponse(status=200)

def products(request):
	productDicts = []
	products = Product.objects.all()

	for p in products:
		productDicts.append(p.dictValue(request))

	return JsonResponse({"products": productDicts})


@csrf_exempt
def addProductReview(request, productID):

    json_data = json.loads(request.body)

    time.sleep(randint(2,8))

    review = ProductReview()
    review.product = Product.objects.get(id=productID)
    review.author = json_data['author']
    review.content = json_data['content']
    review.save()

    return HttpResponse(status=200)
