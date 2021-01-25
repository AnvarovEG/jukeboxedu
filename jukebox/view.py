from django.shortcuts import redirect
from django.views import View


class RedirectOnMusicView(View):

    def get(self, request):
        return redirect('/music')
