from django.urls import path
from .views import home,login_,backendLogin, logout_,sendMessage
urlpatterns = [
	path('',home),
	path('login/',login_),
	path('results/',backendLogin),
	path('logout/',logout_),
	path('<str:keyy>/',sendMessage),
]