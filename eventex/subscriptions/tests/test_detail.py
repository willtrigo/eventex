"""Test App subscriptions detail."""
from django.test import TestCase
from django.shortcuts import resolve_url as r

from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    """docstring for SubscriptionDetailGet."""

    def setUp(self):
        """Set variables."""
        self.obj = Subscription.objects.create(name='Henrique Bastos',
                                               cpf='12345678901',
                                               email='henrique@bastos.net',
                                               phone='21-996186180')
        self.resp = self.client.get(r('subscriptions:detail', self.obj.pk))

    def test_get(self):
        """GET / must return status code 200."""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_detail.html."""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_content(self):
        """Must have content of the subscription."""
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        """Must have 4 fields."""
        contents = (self.obj.name,
                    self.obj.cpf,
                    self.obj.email,
                    self.obj.phone)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)


class SubscriptionDetailNotFound(TestCase):
    """docstring for SubscriptionDetailNotFound."""

    def test_not_found(self):
        """Detail cannot be found."""
        resp = self.client.get(r('subscriptions:detail', 0))
        self.assertEqual(404, resp.status_code)
