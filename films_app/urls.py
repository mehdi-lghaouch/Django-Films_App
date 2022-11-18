from django.urls import path
from . import views

app_name = 'films_app'

urlpatterns = [
    path('', views.FilmListView.as_view(), name='all'),
    path('films_app/<int:pk>/detail', views.FilmDetailView.as_view(), name='film_detail'),
    path('films_app/create/', views.FilmCreateView.as_view(), name='film_create'),
    path('films_app/<int:pk>/update/', views.FilmUpdateView.as_view(), name='film_update'),
    path('films_app/<int:pk>/delete/', views.FilmDeleteView.as_view(), name='film_delete'),
]
