"""Test App core."""
from django.test import TestCase


class HomeTest(TestCase):
    """docstring for HomeTest."""

    def setUp(self):
        """Set variables."""
        self.resp = self.client.get('/')

    def test_get(self):
        """GET / must return status code 200."""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use index.html."""
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_subscription_link(self):
        """Must have a hyperlink to subscribe."""
        self.assertContains(self.resp, 'href="/inscricao/"')
