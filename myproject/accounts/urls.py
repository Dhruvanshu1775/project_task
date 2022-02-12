from django.urls import path
from .views import *

urlpatterns = [
	path('login/',login,name='login'),
	path('register/',Register,name='register'),
	path('logout/', logout, name='logout'),
	path('dashboard/', dashboard, name='dashboard'),
]