"""Test App subscriptions send mail."""
from django.core import mail
from django.test import TestCase

from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    """docstring for post of subscribe."""

    def setUp(self):
        """Set variables."""
        data = dict(name='Henrique Bastos', cpf='12345678901', email='henrique@bastos.net', phone='21-99618-6180')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subcription_email_subject(self):
        """Valid Subject mail."""
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subcription_email_from(self):
        """Valid sender self.email."""
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subcription_email_to(self):
        """Valid to contact self.email."""
        expect = ['contato@eventex.com.br', 'henrique@bastos.net']
        self.assertEqual(expect, self.email.to)

    def test_subcription_email_body(self):
        """Valid email body, should to have 4 fields."""
        contents = ['Henrique Bastos',
                    '12345678901',
                    'henrique@bastos.net',
                    '21-99618-6180']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
