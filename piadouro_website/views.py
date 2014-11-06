from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from piadouro_website.models import Piado
from piadouro_website.forms import FormItemPiado
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.
@login_required
def home(request):
	return render_to_response("piadouro_website/home.html", {"piados": Piado.objects.all(), 'user':request.user})

@login_required
def piado_add(request):
	if(request.method == 'POST'):
		form = FormItemPiado(request.POST, request.FILES)
		if(form.is_valid()):
			piado = form.save(commit=False)
			piado.user = request.user
			piado.save();
			return HttpResponseRedirect('/')
		else:
			pass
	else:
		form = FormItemPiado()
	return render(request, 'piadouro_website/new_piado.html', {'form' : form})

def sair(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required
def meus_piados(request):
	return render_to_response("piadouro_website/home.html", {"piados": Piado.objects.filter(user=request.user), "user": request.user })

@login_required
def users(request):
	return render_to_response("piadouro_website/users.html", {"users": User.objects.all(), "user": request.user})

@login_required
def profile(request, username):
	prof = get_object_or_404(User, username=username)
	
	if "Follow" in request.GET:
		if request.GET['follow'] == 'Follow':
			follow = Follow()
			follow.followed_user = user
			follow.follower_user = request.user
			follow.save()
		else:
			follow = Follow.objects.filter(followed_user__username=username,
											follower_user=request.user)[0]
			follow.delete()

		return HttpResponseRedirect("/user/" + user.name + "/")

	followed = len(Follow.objects.filter(followed_user=username, follower_user=request.user)) > 0

	return render_to_response("piadouro_website/profile.html", {"user": request.user,
																"piados": Piado.objects.filter(user=prof),
																"followed": followed})
