from django.contrib import admin
from .models import Client,Quotation,Item

# Register your models here.
admin.site.register(Client)
admin.site.register(Quotation)
admin.site.register(Item)