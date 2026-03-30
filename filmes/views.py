from django.http import JsonResponse
from .models import Filme

def listar_filmes(request):
    filmes = list(Filme.objects.values())
    return JsonResponse(filmes, safe=False)

def filmes_assistidos(request):
    filmes = list(Filme.objects.filter(status='A').values())
    return JsonResponse(filmes, safe=False)