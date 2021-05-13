from django.shortcuts import render
from .models import Solider, Gun, Platoon


def index(request):

    pocet_vojaku = Solider.objects.all().count()
    vojaci = Solider

    context = {
        'pocet vojaku': pocet_vojaku,
        'vojak': vojaci
    }
    return render(request, 'index.html', context=context)

