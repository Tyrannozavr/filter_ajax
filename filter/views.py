from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Table, Genre
from time import time
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger, EmptyPage

def index(request):
    now = time()
    genres = Genre.objects.all()
    return render(request, 'filter/index.html', {'genres': genres, 'now': now})

class JsonFilterMoviesView(ListView):
    model = Table
    paginate_by = 5
    """Фильтр фильмов в json"""
    def get_queryset(self):
        fields = {'1': 'title', '2': 'count', '3': 'distance'}
        column = fields.get(self.request.GET.get('title'))
        condition = self.request.GET.get('count')
        value = self.request.GET.get('value')
        queryset = Table.objects.all()
        if condition == '1':
            queryset = Table.objects.all().extra(where=[f'{column} > {value}'])
        elif condition == '2':
            queryset = Table.objects.extra(where=[f'{column} < {value}'])
        elif condition == '3':
            queryset = Table.objects.extra(where=[f'{column} = {value}'])
        elif condition == '4':
            queryset = Table.objects.extra(where=[f'{column} LIKE "%{value}%"'])
        return queryset.distinct().values('title', 'date', 'count', 'distance')

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        paginator = Paginator(queryset, self.paginate_by)
        page = request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        queryset = list(queryset)
        # queryset = list(self.get_queryset())
        # print(queryset)
        return JsonResponse({"movies": queryset, 'page': page}, safe=False)
