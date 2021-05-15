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

    zbrane = Gun.objects.order_by('-name')
    zbrane_pocet = Gun.objects.all().count()

    context = {
        'zbrane_pocet': zbrane_pocet,
        'zbrane': zbrane
    }
    return render(request, 'guns.html', context=context)

def platoons(request):

    pocet_praporu = Platoon.objects.all().count()
    prapory = Platoon.objects.order_by('-name')

    context = {
        'pocet_praporu': pocet_praporu,
        'prapory': prapory
    }
    return render(request, 'platoons.html', context=context)


