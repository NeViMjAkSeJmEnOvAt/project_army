from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('soliders', soliders, name='soliders'),
    path('guns', guns, name='guns'),
    path('platoons', platoons, name='platoons'),
    path('ranks', ranks, name='ranks'),
    path('ammo', ammo, name='ammo'),
    path('a1', a1, name='a1'),
    path('a2', a2, name='a2'),
    path('a3', a3, name='a3'),
    path('a4', a4, name='a4'),
    path('a5', a5, name='a5'),
]