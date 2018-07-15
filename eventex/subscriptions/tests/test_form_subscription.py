"""Test App form subscriptions."""
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    """docstring for SubscriptionFormTest."""

    def setUp(self):
        """Set variables."""
        self.form = SubscriptionForm()

    def test_form_has_fields(self):
        """Form must have 4 fields."""
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))
