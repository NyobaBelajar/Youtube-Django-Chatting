from django.urls import path
from .consumer import(
		ChattingSock,		
	)

urlpattern_socket = [
	path('chat/<str:room>/',ChattingSock.as_asgi()),
]