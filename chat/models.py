from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Messages(models.Model):	
	sender = models.ForeignKey(User,related_name='sender',on_delete=models.CASCADE)
	recive = models.ForeignKey(User,related_name='recive',on_delete=models.CASCADE)
	konten = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['created_at']


class RoomChatting(models.Model):
	pengirim = models.ForeignKey(User,related_name='pengirim',on_delete=models.CASCADE)
	penerima = models.ForeignKey(User,related_name='penerima',on_delete=models.CASCADE)
	kode_chat = models.TextField(unique=True)