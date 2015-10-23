from django.db import models


class Grupo(models.Model):
	letra = models.CharField(max_length=1, unique=True)

	def __str__(self):
		return "Grupo " + self.letra

	def __unicode__(self):
		return "Grupo " + self.letra


class Equipo(models.Model):
	nombre = models.CharField(max_length=100)
	grupo = models.ForeignKey(Grupo, related_name='equipos')
	codigo_pais_bandera = models.CharField(max_length=4, default='')

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre
