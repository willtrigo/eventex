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
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(label='telefone', required=False)

    def clean_name(self):
        """Field name should be organizade."""
        name = self.cleaned_data['name']

        # simple way to capitalize the name
        # words = []
        # for w in name.slip():
        #     words.append(w.capitalize())

        # list comprehension
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    def clean(self):
        """Last validation of the form, if necessary the last validation, should be implemented."""
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone.')

        return self.cleaned_data
