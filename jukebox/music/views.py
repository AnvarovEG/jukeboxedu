from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View

from .forms import ArtistForm, AlbumForm
from .models import (Track,
                     Artist,
                     Album)


class IndexView(View):

    def get(self, request):
        # music_list = [
        #     'Blinding Lights. The Weeknd.',
        #     'Circles. Post Malone.',
        #     'The Box.Roddy Ricch.',
        #     'Don\'t Start Now. Dua Lipa.',
        #     'Rockstar.DaBaby Featuring Roddy Ricch.',
        #     'Adore You.Harry Styles.',
        #     'Life Is Good.Future Featuring Drake.',
        #     'Memories.Maroon 5.',
        # ]

        fwd_sort = False
        music_list = []
        tracks = Track.objects.all()

        if fwd_sort:
            tracks = tracks.order_by('rate')
        else:
            tracks = tracks.order_by('-rate')

        for track in tracks:
            music_list.append(f'{track.artist.name}. {track.title}. {track.year} год.')
            artist = Artist.objects.filter(id=2).first()
        return render(request, 'index.html', {'music_list': music_list,
                                              'artist': artist})


class AboutView(View):

    def get(self, request):
        return render(request, 'about.html')


class ArtistsView(View):

    def get(self, request):
        artists = Artist.objects.all()
        return render(request, 'artists/list.html', {'artists_list': artists})


class ArtistView(View):

    def get(self, request, id):
        artist = Artist.objects.filter(id=id).first()

        if not artist:
            # После функции return будет выход и дальше код не пойдет
            return Http404('Исполнитель не найден')

        albums = artist.albums.order_by('year').all()
        return render(request, 'artists/detail.html', {'artist': artist, 'albums': albums})


class AddArtistView(View):

    def get(self, request):
        form = ArtistForm()
        return render(request, 'artists/add.html', {'form': form})

    def post(self, request):
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = Artist(name=form.name,
                            start_year=form.start_year)
            artist.save()
            return redirect('/music/artists')

        return render(request, 'artists/add.html', {'form': form})


class AlbumsView(View):

    def get(self, request):
        albums = Album.objects.all()
        return render(request, 'albums/list.html', {'albums_list': albums})


class AddAlbumView(View):

    def get(self, request):
        form = AlbumForm()
        return render(request, 'albums/add.html', {'form': form})

    def post(self, request):
        form = AlbumForm(request.POST)

        if form.is_valid():
            artist = Artist.objects.filter(id=form.data.get('artist')).first()
            album = Album(title=form.data.get('title'),
                          year=form.data['year'],  # это dict поэтому либо [] либо .get()
                          artist=artist)
            album.save()
            return redirect('/music/albums')

        return render(request, 'albums/add.html', {'form': form})
