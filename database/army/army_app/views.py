from django.shortcuts import render
from .models import Solider, Gun, Platoon, Ranks, Ammo


def index(request):

    pocet_vojaku = Solider.objects.all().count()
    vojaci = Solider.objects.order_by('-name')
    pocet_aktivnich = Solider.objects.filter(activity=True).count()

    context = {
        'pocet_vojaku': pocet_vojaku,
        'vojaci': vojaci,
        'pocet_aktivnich': pocet_aktivnich
    }
    return render(request, 'index.html', context=context)


def soliders(request):

    pocet_vojaku = Solider.objects.all().count()
    vojaci = Solider.objects.order_by('-name')
    pocet_aktivnich = Solider.objects.filter(activity=True).count()

    context = {
        'pocet_vojaku': pocet_vojaku,
        'vojaci': vojaci,
        'pocet_aktivnich': pocet_aktivnich
    }
    return render(request, 'soliders.html', context=context)

def guns(request):

    zbrane = Gun.objects.order_by('-name')
    zbrane_pocet = Gun.objects.all().count()
    #naboje_762 = Gun.objects.filter(ammo_type="7,62").count()
    #naboje_556 = Gun.objects.filter(ammo_type="5,56").count()
    #naboje_9 = Gun.objects.filter(ammo_type="9").count()

    context = {
        'zbrane_pocet': zbrane_pocet,
        'zbrane': zbrane,
        #'naboje_762': naboje_762,
        #'naboje_556': naboje_556,
        #'naboje_9': naboje_9
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

def ranks(request):

    hodnosti = Ranks.objects.order_by('score')

    context = {
        'hodnosti': hodnosti
    }
    return render(request, 'ranks.html', context=context)

def ammo(request):

    naboje = Ammo.objects.order_by('-name')

    context = {
        'naboje': naboje
    }
    return render(request, 'ammo.html', context=context)

# //////////////////////////////////////////////////////////////////////////////// #


def a1(request):

    naboje = Ammo.objects.filter(name="40 mm")

    context = {
        'naboje': naboje
    }
    return render(request, 'ammo_sites/mm40.html', context=context)


def a2(request):

    naboje = Ammo.objects.filter(name="7,62 x 51mm NATO")

    context = {
        'naboje': naboje
    }
    return render(request, 'ammo_sites/nato762.html', context=context)


def a3(request):

    naboje = Ammo.objects.filter(name="5,56 x 45 mm NATO")

    context = {
        'naboje': naboje
    }
    return render(request, 'ammo_sites/nato556.html', context=context)


def a4(request):

    naboje = Ammo.objects.filter(name="5,7 x 28mm")

    context = {
        'naboje': naboje
    }
    return render(request, 'ammo_sites/ammo57.html', context=context)


def a5(request):

    naboje = Ammo.objects.filter(name="9mm Luger")

    context = {
        'naboje': naboje
    }
    return render(request, 'ammo_sites/luger9.html', context=context)