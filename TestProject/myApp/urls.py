from django.urls import path
from . import views

app_name = 'myApp'

urlpatterns= [
	path('other/',views.other,name='other'),
	path('last/',views.last,name='last'),
]