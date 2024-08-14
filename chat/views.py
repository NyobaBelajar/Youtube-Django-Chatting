from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Messages, RoomChatting
from chat.back.generatekoderoom import gen_kode


@login_required(login_url="/login/")
def home(req):
	data = {
		'kontak' : User.objects.all()
	}
	return render(req,'chat/chat.html',data)

@login_required(login_url='/login/')
def sendMessage(req,keyy):
	user = get_object_or_404(User, username=keyy)
	recive = Messages.objects.filter(recive=req.user.id,sender=user.id)
	sender = Messages.objects.filter(sender=req.user.id,recive=user.id)
	result = recive | sender
	usereck = None

	if RoomChatting.objects.filter(pengirim=req.user.id).first() and RoomChatting.objects.filter(penerima=user.id).first():
		usercek = RoomChatting.objects.filter(pengirim=req.user.id).first() or RoomChatting.objects.filter(penerima=user.id).first()
	elif RoomChatting.objects.filter(penerima=req.user.id).first() and RoomChatting.objects.filter(pengirim=user.id).first():
		usercek = RoomChatting.objects.filter(penerima=req.user.id).first() or RoomChatting.objects.filter(pengirim=ruser.id).first()
	else:
		room = f"{gen_kode()}{req.user.id}{user.id}"
		usercek = RoomChatting.objects.create(pengirim_id=req.user.id,penerima_id=user.id,kode_chat=room)

	# print(usercek.kode_chat)
	# print(result)
	
	data = {
		'kontak' : User.objects.all(),
		'pesan' : result,
		'detail': user,
		'roomchat':usercek
	}
	return render(req,'chat/send.html',data)

def login_(req):
	return render(req,'chat/login.html')

def backendLogin(req):
	if req.method == 'POST':
		username = req.POST['username']
		password = req.POST['password']
		result = authenticate(username=username,password=password)
		if result is not None:
			login(req,result)
			return redirect('/')
		else:
			return redirect('/')
	return redirect('/')

def logout_(req):
	logout(req)
	return redirect('/login/')
