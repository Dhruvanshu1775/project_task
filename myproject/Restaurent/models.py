from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DateTimeMixin(models.Model):
	create_at = models.DateTimeField(auto_now_add = True)
	update_at = models.DateTimeField(auto_now = True)

	class meta:
		abstract = True


class Restaurent(DateTimeMixin):
	name = models.CharField(max_length = 200)
	owner_key = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
	address = models.TextField(null = True, blank = True)
	photo = models.ImageField(null = True, blank = True, upload_to = 'media')
	phone = models.IntegerField(null = True, blank = True)

	def __str__(self):
		return self.name

class Dish(DateTimeMixin):
	restaurent_key = models.ForeignKey(Restaurent, on_delete = models.CASCADE, null = True, blank = True)
	name           = models.CharField(max_length = 250)
	price          = models.IntegerField()

	def __str__(self):
		return str(self.restaurent_key)

class OrderStatus(DateTimeMixin):
	status = models.CharField(max_length = 200) 

	def __str__(self):
		return self.status

class Order(DateTimeMixin):
	user_key       = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
	restaurent_key = models.ForeignKey(Restaurent, on_delete = models.CASCADE, null = True, blank = True)
	dish_key       = models.ForeignKey(Dish, on_delete = models.CASCADE, null = True, blank = True)
	status         = models.ForeignKey(OrderStatus,on_delete = models.CASCADE, null = True, blank = True )
	quantity       = models.IntegerField()
	amount         = models.IntegerField()

	def __str__(self):
		return str(self.restaurent_key)


