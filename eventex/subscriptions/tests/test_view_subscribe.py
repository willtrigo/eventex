"""Test App subscriptions."""
from django.core import mail
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscribeGet(TestCase):
    """docstring for SubscribeTest."""

    def setUp(self):
        """Set variables."""
        self.resp = self.client.get('/inscricao/')

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


class SubscribePostValid(TestCase):
    """docstring for post of subscribe."""

    def setUp(self):
        """Set variables."""
        data = dict(name='Henrique Bastos', cpf='12345678901', email='henrique@bastos.net', phone='21-99618-6180')
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        """Valid POST should redirect to /inscricao/."""
        self.assertEqual(302, self.resp.status_code)

    def test_send_subcribe_email(self):
        """Valid SEND should have 1 sending."""
        self.assertEqual(1, len(mail.outbox))


class SubscribePostInvalid(TestCase):
    """docstring for invalid post of subscribe."""

    def setUp(self):
        """Set variables."""
        self.resp = self.client.post('/inscricao/', {})

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


class SubscribeSuccessMessage(TestCase):
    """docstring for post of subscribe success message."""

    def setUp(self):
        """Set variables."""
        data = dict(name='Henrique Bastos', cpf='12345678901', email='henrique@bastos.net', phone='21-99618-6180')
        self.resp = self.client.post('/inscricao/', data, follow=True)

    def test_message(self):
        """Subscribe must have confirmation."""
        self.assertContains(self.resp, 'Inscrição realizada com sucesso!')
