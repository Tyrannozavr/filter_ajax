from django.urls import path
from .views import index, JsonFilterMoviesView




urlpatterns = [
    path('', index, name='index'),
    path('json_filter/', JsonFilterMoviesView.as_view(), name='json_filter')
]