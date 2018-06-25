from django import forms


class SubscriptionForm(forms.Form):
    """docstring for SubscriptionForm, have 4 fiels."""
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='telefone')
