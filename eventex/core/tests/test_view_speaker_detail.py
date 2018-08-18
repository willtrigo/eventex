"""Docstring view for speakers."""
from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.core.models import Speaker


class SpeakerDetailGet(TestCase):
    """Get detail of speaker."""

    def setUp(self):
        """Set variables."""
        Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            photo='http://hbn.link/hopper-pic',
            website='http://hbn.link/hopper-site',
            description='Programadora e almirante.'
        )
        self.resp = self.client.get(r('speaker_detail', slug='grace-hopper'))

    def test_get(self):
        """GET should return status 200."""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use speaker_detail.html."""
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        """Html must contain information about the speaker."""
        contents = [
            'Grace Hopper',
            'Programadora e almirante',
            'http://hbn.link/hopper-pic',
            'http://hbn.link/hopper-site'
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_context(self):
        """Speaker must be in context."""
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)


class SpeakerDetailNotFound(TestCase):
    """Detail of the speaker is not found."""

    def test_not_found(self):
        """Should return 404."""
        response = self.client.get(r('speaker_detail', slug='not-found'))
        self.assertEqual(404, response.status_code)
