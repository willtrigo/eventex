"""Test App subscriptions viem."""
from django.core import mail
from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscribeNewGet(TestCase):
    """docstring for SubscribeTest."""

    def setUp(self):
        """Set variables."""
        self.resp = self.client.get(r('subscriptions:new'))

    def test_get(self):
        """GET / must return status code 200."""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_form.html."""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        """Html must contain input tags."""
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1),
                )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        """Html must contain csrf."""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form."""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscribeNewPostValid(TestCase):
    """docstring for post of subscribe."""

    def setUp(self):
        """Set variables."""
        data = dict(name='Henrique Bastos', cpf='12345678901', email='henrique@bastos.net', phone='21-99618-6180')
        self.resp = self.client.post(r('subscriptions:new'), data)

    def test_post(self):
        """Valid POST should redirect to r('subscriptions:detail', 1)."""
        self.assertRedirects(self.resp, r('subscriptions:detail', 1))

    def test_send_subcribe_email(self):
        """Valid SEND should have 1 sending."""
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        """Valid Save should have fields."""
        self.assertTrue(Subscription.objects.exists())


class SubscribeNewPostInvalid(TestCase):
    """docstring for invalid post of subscribe."""

    def setUp(self):
        """Set variables."""
        self.resp = self.client.post(r('subscriptions:new'), {})

    def test_post(self):
        """Invalid POST should not redirect."""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_form.html."""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        """Context must have subscription form."""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_erros(self):
        """Context must have errors of form."""
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        """Don't Save subscription."""
        self.assertFalse(Subscription.objects.exists())


class TemplateRegressionTest(TestCase):
    """docstring for TemplateRegressionTest of subscribe."""

    def test_template_has_non_field_errors(self):
        """Template must should be show the error."""
        invalid_data = dict(name='Henrique Bastos', cpf='12345678901')
        response = self.client.post(r('subscriptions:new'), invalid_data)

        self.assertContains(response, '<ul class="errorlist nonfield">')
