from django.shortcuts import render
from .models import Solider, Gun, Platoon


def index(request):

    pocet_vojaku = Solider.objects.all().count()
    vojaci = Solider.objects.order_by('-name')
    pocet_aktivnich = Solider.objects.filter(activity = True).count()

    context = {
        'pocet_vojaku': pocet_vojaku,
        'vojaci': vojaci,
        'pocet_aktivnich': pocet_aktivnich
    }
    return render(request, 'index.html', context=context)

def guns(request):

    pocet_vojaku = Solider.objects.all().count()
    vojaci = Solider

    context = {
        'pocet vojaku': pocet_vojaku,
        'vojak': vojaci
    }
    return render(request, 'guns.html', context=context)

def platoons(request):

    pocet_vojaku = Solider.objects.all().count()
    vojaci = Solider

    context = {
        'pocet vojaku': pocet_vojaku,
        'vojak': vojaci
    }
    return render(request, 'platoons.html', context=context)


