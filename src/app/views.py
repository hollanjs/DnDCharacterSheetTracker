from django.shortcuts import render
from app.models import *
from django.views.generic import *


def index(request):
    return render(request, 'app/index.html', {})

class CharacterList(ListView):
    model = Character

class CharacterDetail(DetailView):
    model = Character