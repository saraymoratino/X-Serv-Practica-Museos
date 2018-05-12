from django.db import models

# Create your models here.

class museos (models.Model):
	museo = models.TextField()
	id_entidad = models.TextField()
	descripcion = models.TextField()
	horario = models.TextField()
	transporte = models.TextField()
	accesibilidad = models.TextField()
	content_url = models.TextField()

	nombre_via = models.TextField()
	clase_vial = models.TextField()
	tipo_num = models.TextField()
	num = models.TextField()
	localidad = models.TextField()
	provincia = models.TextField()
	codigo_postal = models.TextField()
	barrio = models.TextField()
	distrito = models.TextField()
	coordenada_x = models.TextField()
	coordenada_y = models.TextField()
	latitud = models.TextField()
	longitud = models.TextField()

	telefono = models.TextField()
	fax = models.TextField()
	email = models.TextField()

	descripcion_entidad = models.TextField()

	def __str__self():
		return self.museo

class comentario (models.Model):

	museo = models.ForeignKey(museos)
	usuario = models.TextField()
	fecha = models.TextField()
	texto = models.TextField()