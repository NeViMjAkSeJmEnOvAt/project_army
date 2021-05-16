from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('guns', guns, name='guns'),
    path('platoons', platoons, name='platoons'),
    path('ranks', ranks, name='ranks'),
]