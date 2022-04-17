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
            queryset = Table.objects.raw(f'''
                SELECT * FROM table_table
                WHERE {column} > {value};
                ''').all
        elif condition == '2':

            queryset = Table.objects.raw(f'''-- 
        --                 SELECT * FROM table_table
        --         #         WHERE {column} < {value};
                        ''')
        elif condition == '3':
            f = Table.objects.raw(f'''
                        SELECT * FROM table_table
                        WHERE {column} = {value};
                        ''')
        elif condition == '4':
            queryset = Table.objects.raw(f'''
                    SELECT * FROM table_table
                    WHERE {column} LIKE "%{value}%";''')
        print(queryset)
        queryset = Table.objects.all().distinct().values("title")
        print(queryset)
        return queryset
        # return queryset.distinct().values('title')

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"movies": queryset}, safe=False)


