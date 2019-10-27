from django.urls import path
from core import views

urlpatterns = [
	path('', views.home, name='core_home'),
	path('contato/', views.contact, name='core_contact'),
]