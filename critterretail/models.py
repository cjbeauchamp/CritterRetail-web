from django.db import models
import json

class Product(models.Model):
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.CharField(max_length=50)

    def dictValue(self, request):
    	return {
    		"name": self.name,
    		"price": float(self.price),
    		"productID": self.id,
    		"description": self.description,
    		"image": request.scheme + "://" + request.get_host() + "/static/products/" + self.image + ".jpg",
    	}


    def jsonValue(self, request):
    	return json.dumps(self.dictValue(request))

    def __unicode__(self):
        return u'%s' % (self.name)

class ProductReview(models.Model):
	product = models.ForeignKey('Product')
	author = models.CharField(max_length=50)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

class ProductRating(models.Model):
	product = models.ForeignKey('Product')
	rating = models.IntegerField(max_length=50)
	created = models.DateTimeField(auto_now_add=True)
