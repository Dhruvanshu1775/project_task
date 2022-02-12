from django.urls import path
from .views import *

urlpatterns = [
	path('add_restaurent/', createRestaurant, name='add_restaurent'),
	path('restaurent_list/', restaurent_list, name='restaurent_list'),
	path('place_order/<int:id>', place_order, name='place_order'),
	path('add_dish/<int:id>', add_dish, name='add_dish'),
	path('order_list/<int:id>',order_list, name='order_list'),
	path('update_order/<int:id>',update_order, name='update_order'),

]