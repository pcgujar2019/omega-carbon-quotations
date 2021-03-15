from django.forms import ModelForm
from .models import Client

class AddNewClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'address', 'email', 'contact']