from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def createRestaurant(request):
	

	if request.method == 'POST' and request.FILES['photo']:

		name = request.POST['name']
		address = request.POST['address']
		phone = request.POST['phone']
		image = request.FILES['photo']
		Restaurent.objects.create(name = name , address = address, photo = image, phone = phone, owner_key = request.user)
		return redirect('add_restaurent')
	restaurent_obj = Restaurent.objects.filter(owner_key = request.user)	

	context = {
		'restaurent_obj':restaurent_obj,
	}

	return render(request, 'restaurent.html', context)


def restaurent_list(request):
	restaurent_obj = Restaurent.objects.all()

	context = {
		'restaurent_obj':restaurent_obj,
	}

	return render(request, 'restaurent.html', context)



def place_order(request, id):
	from django.contrib import messages

	dish_obj = Dish.objects.filter(restaurent_key = id)
	restaurent_obj = Restaurent.objects.get(pk = id)


	if request.method == 'POST':
		name = request.POST['dish']
		quantity = request.POST['Quantity']
		dish_instance = Dish.objects.get(pk = name)
		order_status = OrderStatus.objects.get(pk = 10)

		amount_total = int(quantity) * int(dish_instance.price)

		Order.objects.create(user_key = request.user, restaurent_key = restaurent_obj, dish_key = dish_instance, quantity = quantity, amount = amount_total, status = order_status)
		messages.add_message(request, messages.INFO, 'Order Succesfull.')

		return redirect('place_order', restaurent_obj.id)

	order_obj = Order.objects.filter(user_key = request.user, restaurent_key = id)


	context = {
		'order_obj':order_obj,
		'dish_obj':dish_obj,
		'restaurent_obj':restaurent_obj,
	}

	return render(request, 'order.html', context)


def add_dish(request, id):
	restaurent_obj = Restaurent.objects.get(pk = id)

	if request.method == 'POST':
		name = request.POST['name']
		price = request.POST['price']

		Dish.objects.create(restaurent_key = restaurent_obj, name = name, price = price)
		return redirect('add_dish',restaurent_obj.id)

	dish_obj = Dish.objects.filter(restaurent_key = id)


	context = {
		'dish_obj':dish_obj,
		'restaurent_obj':restaurent_obj,
	}

	return render(request, 'dish.html', context)


def order_list(request, id):
	restaurent_obj = Restaurent.objects.get(pk = id)

	order_obj = Order.objects.filter(restaurent_key = id)
	status_obj = OrderStatus.objects.all()

	if request.method == 'POST':
		name = request.POST['status']
		if name == "All":
			order_obj = Order.objects.filter(restaurent_key = id)
		else:
			order_obj = Order.objects.filter(restaurent_key = id, status = name)

	context = {
		'order_obj':order_obj,
		'restaurent_obj':restaurent_obj,
		'status_obj':status_obj,
	}

	return render(request, 'order_list.html', context)

def update_order(request, id):

	order_obj = Order.objects.get(pk = id)
	status_obj = OrderStatus.objects.all()


	if request.method == 'POST':
		status = request.POST['status']
		status_instance = OrderStatus.objects.get(pk = status)
		order_obj.status = status_instance
		order_obj.save()
		return redirect('order_list',order_obj.restaurent_key.id)

	context = {
		'order_obj':order_obj,
		'status_obj':status_obj
	}	

	return render(request, 'update_order.html', context)


# def search_status(request, id):
# 	restaurent_obj = Restaurent.objects.get(pk = id)

# 	if request.method == 'GET':
# 		name = request.GET['status']
# 		order_obj = Order.objects.filter(restaurent_key = id, status = name)

# 		context = {
# 			''
# 		}

# 		return render(request,'order_list.html')


# 	return redirect()