from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='music_index'),
    path('about/', views.AboutView.as_view(), name='music_about'),
    path('artists/', views.ArtistsView.as_view(), name='music_artists'),
    path('artists/add/', views.AddArtistView.as_view(), name='music-artist-add')
]
