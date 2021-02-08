from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='music_index'),
    path('about/', views.AboutView.as_view(), name='music_about'),

    path('artists/', views.ArtistsView.as_view(), name='music_artists'),
    path('artist/<int:id>', views.ArtistView.as_view(), name='music_artist'),
    path('artists/add/', views.AddArtistView.as_view(), name='music-artist-add'),

    path('albums/', views.AlbumsView.as_view(), name='music_albums'),
    path('albums/add/', views.AddAlbumView.as_view(), name='music_album-add')
]
