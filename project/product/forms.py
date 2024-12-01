from .models import CustomUser
from django.forms import ModelForm


class WalletForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['value']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.instance.author = user