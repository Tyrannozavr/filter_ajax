from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Table, Genre
from time import time

def index(request):
    now = time()
    genres = Genre.objects.all()
    return render(request, 'filter/index.html', {'genres': genres, 'now': now})


class JsonFilterMoviesView(ListView):
    """Фильтр фильмов в json"""
    def get_queryset(self):
        # queryset = Movie.objects.filter(
        #     Q(year__in=self.request.GET.getlist("year")) |
        #     Q(genres__in=self.request.GET.getlist("genre"))
        # ).distinct().values("title", "tagline", "url", "poster")
        queryset = Table.objects.all().distinct().values("title")
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"movies": queryset}, safe=False)