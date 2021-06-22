from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('soliders', soliders, name='soliders'),
    path('soliders/<int:pk>/update/', SoliderEdit.as_view(), name='soliders-edit'),
    path('soliders/<int:pk>/delete/', SoliderDelete.as_view(), name='soliders-delete'),
    path('soliders/create/', SoliderCreate.as_view(), name='soliders-create'),
    path('guns', guns, name='guns'),
    path('platoons', platoons, name='platoons'),
    path('ranks', ranks, name='ranks'),
    path('ammo', AmmoListView.as_view(), name='ammo'),
    path('ammo/<int:pk>/', AmmoDetailView.as_view(), name='ammo_detail')

]