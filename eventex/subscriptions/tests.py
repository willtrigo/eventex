"""Test App subscriptions."""
from django.core import mail
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
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
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """Html must contain csrf."""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form."""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """Form must have 4 fields."""
        form = self.resp.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))


class SubscribePostTest(TestCase):
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

    def test_subcription_email_subject(self):
        """Valid Subject mail."""
        email = mail.outbox[0]
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, email.subject)

    def test_subcription_email_from(self):
        """Valid sender email."""
        email = mail.outbox[0]
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, email.from_email)

    def test_subcription_email_to(self):
        """Valid to contact email."""
        email = mail.outbox[0]
        expect = ['contato@eventex.com.br', 'henrique@bastos.net']

        self.assertEqual(expect, email.to)

    def test_subcription_email_body(self):
        """Valid email body, should to have 4 fields."""
        email = mail.outbox[0]

        self.assertIn('Henrique Bastos', email.body)
        self.assertIn('12345678901', email.body)
        self.assertIn('henrique@bastos.net', email.body)
        self.assertIn('21-99618-6180', email.body)


class SubscribeInvalidPost(TestCase):
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
