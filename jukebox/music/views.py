from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import ArtistForm
from .models import (Track,
                     Artist)


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


class AddArtistView(View):

    def get(self, request):
        form = ArtistForm()
        return render(request, 'artists/add.html', {'form': form})

    def post(self, request):
        artist_name = request.POST.get('name')
        artist_start_year = int(request.POST.get('start_year'))

        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = Artist(name=artist_name,
                            start_year=artist_start_year)
            artist.save()
            return redirect('/music/artists')

        return render(request, 'artists/add.html', {'form': form})
