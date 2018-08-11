"""Test App core."""
from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    """docstring for HomeTest."""

    def setUp(self):
        """Set variables."""
        self.resp = self.client.get(r('home'))

    def test_get(self):
        """GET / must return status code 200."""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use index.html."""
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_subscription_link(self):
        """Must have a hyperlink to subscribe."""
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.resp, expected)
