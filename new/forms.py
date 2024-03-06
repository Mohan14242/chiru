from django.forms import ModelForm
from .models import room

class roomform(ModelForm):
    class Meta:
        model=room
        fields='__all__'
