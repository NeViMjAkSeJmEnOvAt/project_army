from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('soliders', soliders, name='soliders'),
    path('guns', guns, name='guns'),
    path('platoons', platoons, name='platoons'),
    path('ranks', ranks, name='ranks'),
    path('ammo', AmmoListView.as_view(), name='ammo'),
    path('ammo/<int:pk>/', AmmoDetailView.as_view(), name='ammo_detail')

]