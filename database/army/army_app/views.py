from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Solider, Gun, Platoon, Ranks, Ammo
from .forms import *
from django.urls import reverse_lazy

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


class SoliderEdit(LoginRequiredMixin, UpdateView, PermissionRequiredMixin):
    model = Solider
    template_name = 'edit.html'
    form_class = EditSolider
    login_url = '/account/login'
    permission_required = 'army_app.change_solider'


class SoliderCreate(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    model = Solider
    fields = ['name', 'date_of_birth', 'score_run', 'score_pushup', 'score_situp', 'rank', 'weapon', 'activity', 'country']
    template_name = 'create.html'
    login_url = '/account/login'
    permission_required = 'army_app.create_solider'


class SoliderDelete(LoginRequiredMixin, DeleteView, PermissionRequiredMixin):
    model = Solider
    success_url = reverse_lazy('soliders')
    template_name = 'delete.html'
    login_url = '/account/login'
    permission_required = 'army_app.delete_solider'

