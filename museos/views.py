from django.shortcuts import render
from .models import museos
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .parse import create_BD
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.contrib.auth import authenticate, login
import urllib


# Create your views here.

@csrf_exempt
def pag_principal(request):

	museos_BD = create_BD()

	recurso = request.method
	print(str(recurso))

	if recurso == 'GET':
		#Tengo que coger de 5 en 5 los museos.

		context = {'museos_BD': museos_BD}
		template = get_template('pag_principal.html')
		return HttpResponse(template.render(Context(context)))


	elif recurso == 'POST':
		valor = request.POST.get("submit")
		if valor == 'Login':
			usuario = request.POST.get("usuario")
			contraseña = request.POST.get("contraseña")
			print("Usuario: " + str(usuario) + " Contraseña: " + str(contraseña))

			user = authenticate(username=usuario, password=contraseña)
			if user == None:

				context = {'museos_BD': museos_BD, 'user': user}
				template = get_template('pag_principal.html')
				return HttpResponse(template.render(Context(context)))
			else:

				context = {'museos_BD': museos_BD, 'user': user}
				template = get_template('pag_principal.html')
				return HttpResponse(template.render(Context(context)))

		elif valor == 'Register':
			usuario = request.POST.get("usuario")
			contraseña = request.POST.get("contraseña")
			context = {'museos_BD': museos_BD} #Deberia de mostrar de 5 en 5
			template = get_template('pag_principal.html')
			return HttpResponse(template.render(Context(context)))
		else:
			num_accesible = int(request.POST.get("num_accesible"))
			mus_accesibles = []

			for museum in museos_BD:
				access = museum.accesibilidad
				if int(access) == 1:
					mus_accesibles.append(museum)

			context = {'museos_BD': museos_BD, 'mus_accesibles': mus_accesibles, 'num_accesible': num_accesible} #Deberia de mostrar de 5 en 5
			template = get_template('pag_principal.html')
			return HttpResponse(template.render(Context(context)))


	else:
		return HttpResponse("Recurso no válido")



@csrf_exempt
def mostrar_museos(request):
	museos_BD = create_BD()
	recurso = request.method
	distritos = []
	for museum in museos_BD:
		distrito = museum.distrito
		if distrito in distritos:
			pass
		else:
			distritos.append(distrito)

	if recurso == 'GET':
		distrito_select = 'TODOS LOS MUSEOS DE MADRID'
		context = {'museos_BD': museos_BD, 'distritos': distritos, 'distrito_select': distrito_select}
		template = get_template('total_museos.html')
		return HttpResponse(template.render(Context(context)))

	else: #Para el POST
		value = request.POST.get("distrito_v")
		museos_distrito = []
		if int(value) == 0:
			dist = 0
			museos_distrito = museos_BD
			distrito_select = 'TODOS LOS MUSEOS DE MADRID'
		else:
			dist = 1
			distrito_select = distritos[int(value)-1]
			for museum in museos_BD:
				dist = museum.distrito
				if dist == distrito_select:
					museos_distrito.append(museum)

		context = {'museos_BD': museos_distrito, 'distritos': distritos, 'dist': dist, 'distrito_select':distrito_select}
		template = get_template('total_museos.html')
		return HttpResponse(template.render(Context(context)))





def info_museo(request, idx):
	museos_BD = create_BD()
	mus = []
	for museum in museos_BD:
		if idx == str(museum.id):
			mus = museum

	context = {'mus': mus, 'indice': idx}
	template = get_template('info_museo.html')
	return HttpResponse(template.render(Context(context)))

def about(request):
	template = get_template('about.html')
	return HttpResponse(template.render(Context()))
