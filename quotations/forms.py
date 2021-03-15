from django.forms import ModelForm
from .models import Client, Quotation, Item

class AddNewClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'address', 'email', 'contact']

class AddItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'size', 'quantity', 'rate', 'hsncode', ]

class AddQuotationForm(ModelForm):
    class Meta:
        model = Quotation
        fields = ['reference', 'dated', 'salutation', 'subject', 'introduction', 'closing', 'signature', 'termsnconditions']