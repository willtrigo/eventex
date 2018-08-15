"""docstring for subscription forms."""
from django import forms
from django.core.exceptions import ValidationError


def validate_cpf(value):
    """CPF must have only numbers."""
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números.', 'digits')

    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 números.', 'length')


class SubscriptionForm(forms.Form):
    """Subscription form have 4 fiels."""

    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='telefone')
