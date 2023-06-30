from django import forms
from . models import *

class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = "__all__"
        widgets = {
         'name':forms.TextInput(attrs=({'placeholder':'Enter Coffee Name....', 'class':'custom_input'})),
         'price':forms.TextInput(attrs=({'placeholder':'Enter Price....', 'class':'custom_input'})),
         'quantity':forms.TextInput(attrs=({'placeholder':'Enter quantity.....', 'class':'custom_input'})),
         'image':forms.FileInput(attrs=({'class':'custom_input'})),
        }