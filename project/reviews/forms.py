from django.forms import ModelForm
from .models import Review

class TodoForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title','memo']

