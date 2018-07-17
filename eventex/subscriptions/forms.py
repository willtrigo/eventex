"""docstring for subscription forms."""
from django import forms


class SubscriptionForm(forms.Form):
    """Subscription form have 4 fiels."""

    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='telefone')
