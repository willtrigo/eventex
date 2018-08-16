"""Docstring models for speakers."""
from django.core.exceptions import ValidationError
from django.test import TestCase

from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    """Validate model contact."""

    def setUp(self):
        """Set variables."""
        self.speaker = Speaker.objects.create(name='Henrique Bastos',
                                              slug='henrique-bastos',
                                              photo='http://hbn.link/hb-pic')

    def test_email(self):
        """Validate creation of the contact with email."""
        contact = Contact.objects.create(speaker=self.speaker,
                                         kind=Contact.EMAIL,
                                         value='henrique@bastos.net')

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        """Validate creation of the contact with phone."""
        contact = Contact.objects.create(speaker=self.speaker,
                                         kind=Contact.PHONE,
                                         value='21-996186180')

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P."""
        contact = Contact.objects.create(speaker=self.speaker,
                                         kind='A',
                                         value='B')

        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        """Validate str."""
        contact = Contact(speaker=self.speaker,
                          kind=Contact.EMAIL,
                          value='henrique@bastos.net')
        self.assertEqual('henrique@bastos.net', str(contact))
