from django.forms import ModelForm
from .models import Solider


class EditSolider(ModelForm):
    class Meta:
        model = Solider
        fields = ['score_run', 'score_pushup', 'score_situp']


class ModelSolider(ModelForm):
    class Meta:
        model = Solider
        fields = '__all__'