"""Docstring models for speakers."""
from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.core.models import Speaker


class SpeakerModelTest(TestCase):
    """Test models of the speaker."""

    def setUp(self):
        """Set variables."""
        self.speaker = Speaker.objects.create(name='Grace Hopper',
                                              slug='grace-hopper',
                                              photo='http://hbn.link/hopper-pic',
                                              website='http://hbn.link/hopper-site',
                                              description='Programadora e almirante.')

    def test_create(self):
        """Test create model."""
        self.assertTrue(Speaker.objects.exists())

    def test_description_can_be_blank(self):
        """Validate attribute of description field to be equal true."""
        field = Speaker._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_website_can_be_blank(self):
        """Validate attribute of website field to be equal true."""
        field = Speaker._meta.get_field('website')
        self.assertTrue(field.blank)

    def test_str(self):
        """Validate str."""
        self.assertEqual('Grace Hopper', str(self.speaker))

    def test_get_absolute_url(self):
        """Discover the real url of the Speaker's website."""
        url = r('speaker_detail', slug=self.speaker.slug)
        self.assertEqual(url, self.speaker.get_absolute_url())
