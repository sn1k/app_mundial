from django.shortcuts import render
from partidos.models import Partido


def ver_partidos(request):
	partidos = Partido.objects.all().order_by('fecha')
	return render(request,'partidos/ver_partidos.html',{ 'partidos':partidos })
