import datetime

from django import forms

from jukebox.music.models import Artist

class ArtistForm(forms.Form):
    name = forms.CharField(label='Название исполнителя', min_length=2, max_length=128, required=True)
    start_year = forms.IntegerField(label='Год основания', min_value=1900, max_value=2022, required=True,
                                    initial=datetime.datetime.today().year)



class AlbumForm(forms.Form):
    title = forms.CharField(label='Название альбома', min_length=1, max_length=128, required=True)
    year = forms.IntegerField(label='Год', min_value=1900, max_value=2022, required=True,
                                    initial=datetime.datetime.today().year)
    artist = forms.ModelChoiceField(queryset=Artist.objects.all(), required=True)
