from django.urls import path
from .views import *

urlpatterns = [
    path('singup/', SignUpView.as_view(), name='singup'),
]