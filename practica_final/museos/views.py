from django.shortcuts import render
from .models import museos
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .parse import create_BD
from django.template import Context
from django.template import RequestContext
from django.template.loader import get_template

# Create your views here.

	
def pag_principal(request):
	
	museos_BD = museos.objects.all()
	create_BD(museos_BD)

	recurso = request.method
	print(str(recurso))

	lista_museos = '<html><body>'
	if recurso == 'GET':
		for parametros in museos.objects.all():
			nombre_museo = parametros.museo
			url = parametros.content_url
			nombre_museo = '<a href=' + url + '>'+ nombre_museo + '</a>'

			clase_vial = parametros.clase_vial
			nombre_via = parametros.nombre_via
			numero = parametros.num
			codigo_postal = parametros.codigo_postal
			localidad = parametros.localidad
			provincia = parametros.provincia
			iden = parametros.id
			direccion = clase_vial + " " + nombre_via + " " + ", Nº " + numero + "- " + codigo_postal + " (" + localidad + ")"

			mas_info =  '<a href=/' + str(iden) + '>Más información</a>' 

			lista_museos = lista_museos + nombre_museo + '<br>' + "DIRECCION: " + direccion + '<br>' + mas_info + '<br><br>'		
		
		return HttpResponse(lista_museos)

	elif recurso == 'POST':
		return HttpResponse("Esto es un POST")

	else:
		return HttpResponse("Recurso no válido")


def info_museos(request, idx):

	museo = museos.objects.get(id = idx).museo
	id_entidad = museos.objects.get(id = idx).id_entidad
	descripcion = museos.objects.get(id = idx).descripcion
	horario = museos.objects.get(id = idx).horario
	transporte = museos.objects.get(id = idx).transporte
	accesibilidad = museos.objects.get(id = idx).accesibilidad
	url = museos.objects.get(id = idx).content_url
	content_url = '<a href=' + url + '>Enlace a la página del museo</a>'
	nombre_via = museos.objects.get(id = idx).nombre_via
	clase_vial = museos.objects.get(id = idx).clase_vial
	tipo_num = museos.objects.get(id = idx).tipo_num
	num = museos.objects.get(id = idx).num
	localidad = museos.objects.get(id = idx).localidad
	provincia = museos.objects.get(id = idx).provincia
	codigo_postal = museos.objects.get(id = idx).codigo_postal
	barrio = museos.objects.get(id = idx).barrio
	distrito = museos.objects.get(id = idx).distrito
	coordenada_x = museos.objects.get(id = idx).coordenada_x
	coordenada_y = museos.objects.get(id = idx).coordenada_y
	latitud = museos.objects.get(id = idx).latitud
	longitud = museos.objects.get(id = idx).longitud
	telefono = museos.objects.get(id = idx).telefono
	fax = museos.objects.get(id = idx).fax
	email = museos.objects.get(id = idx).email
	descripcion_entidad = museos.objects.get(id = idx).descripcion_entidad

	info_total = '<b><a style="color:blue">NOMBRE MUSEO: </a></b>' + museo + '<br>' + '<b><a style="color:blue">ENTIDAD: </a></b>' + id_entidad + '<br>' 
	info_total += '<b><a style="color:blue">DESCRIPCION: </a></b>' + descripcion + '<br>' + '<b><a style="color:blue">HORARIO: </a></b>' + horario + '<br>'
	info_total += '<b><a style="color:blue">TRANSPORTE: </a></b>' + transporte + '<br>' + '<b><a style="color:blue">ACCESIBILIDAD: </a></b>' + accesibilidad + '<br>'
	info_total += '<b><a style="color:blue">URL: </a></b>' + content_url + '<br>' + '<b><a style="color:blue">NOMBRE VIA: </a></b>' + nombre_via + '<br>' 
	info_total += '<b><a style="color:blue">CLASE VIAL: </a></b>' + clase_vial + '<br>' + '<b><a style="color:blue">TIPO NUM: </a></b>' + tipo_num + '<br>'
	info_total += '<b><a style="color:blue">NUMERO: </a></b>' + num + '<br>' + '<b><a style="color:blue">LOCALIDAD: </a></b>' + localidad + '<br>'
	info_total += '<b><a style="color:blue">PROVINCIA: </a></b>' + provincia + '<br>' + '<b><a style="color:blue">CODIGO POSTAL: </a></b>' + codigo_postal + '<br>' 
	info_total += '<b><a style="color:blue">BARRIO: </a></b>' + barrio + '<br>' + '<b><a style="color:blue">DISTRITO: </a></b>' + distrito + '<br>' 
	info_total += '<b><a style="color:blue">COORDENADA X: </a></b>' + coordenada_x + '<br>' + '<b><a style="color:blue">COORDENADA Y: </a></b>' + coordenada_y + '<br>'
	info_total += '<b><a style="color:blue">LATITUD: </a></b>' + latitud + '<br>' + '<b><a style="color:blue">LONGITUD: </a></b>' + longitud + '<br>' 
	info_total += '<b><a style="color:blue">TELEFONO: </a></b>' + telefono + '<br>' + '<b><a style="color:blue">FAX: </a></b>' + fax + '<br>' 
	info_total += '<b><a style="color:blue">EMAIL: </a></b>' + email + '<br>' + '<b><a style="color:blue">DESCRIPCION ENTIDAD: </a></b>' + descripcion_entidad

	return HttpResponse(info_total)

def about (request):
	template = get_template('pag_principal.html')
	return HttpResponse(template.render(Context()))