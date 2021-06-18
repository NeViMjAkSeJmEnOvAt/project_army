from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Solider, Gun, Platoon, Ranks, Ammo


def index(request):
    vojaci = Solider.objects.order_by('name')

    context = {
        'vojaci': vojaci,
    }
    return render(request, 'index.html', context=context)


def soliders(request):

    pocet_vojaku = Solider.objects.all().count()
    vojaci = Solider.objects.order_by('name')
    vojaci_odkonce = Solider.objects.order_by('-name')
    pocet_aktivnich = Solider.objects.filter(activity=True).count()

    context = {
        'pocet_vojaku': pocet_vojaku,
        'vojaci': vojaci,
        'vojaci_odkonce': vojaci_odkonce,
        'pocet_aktivnich': pocet_aktivnich
    }
    return render(request, 'soliders.html', context=context)

def guns(request):

    zbrane = Gun.objects.order_by('name')
    zbrane_pocet = Gun.objects.all().count()

    context = {
        'zbrane_pocet': zbrane_pocet,
        'zbrane': zbrane,
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


class AmmoListView(ListView):
    model = Ammo
    context_object_name = 'naboje'
    template_name = 'ammo.html'


class AmmoDetailView(DetailView):
    model = Ammo
    context_object_name = 'naboj'
    template_name = 'ammo_detail.html'


class EditListView(DetailView):
    model = Solider
    context_object_name = 'vojak'
    template_name = 'edit.html'
