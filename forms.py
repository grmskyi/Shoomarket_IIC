from .models import Client
from django.forms import ModelForm, TextInput


class ClientForm(ModelForm):
    class Meta:
        model= Client
        fields=["name", "surname", "email", "mobile"]
        widgets={
            "name":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введіть імя'

            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть прізвище'

            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть імейл'

            }),
            "mobile": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть номер телефону'

            }),

        }