"""Docstring view for talk list."""
from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.core.models import Talk, Speaker, Course


class TalkListGet(TestCase):
    """Get list of talkers."""

    def setUp(self):
        """Set variables."""
        t1 = Talk.objects.create(
            title='Título da Palestra',
            start='10:00',
            description='Descrição da palestra.'
        )
        t2 = Talk.objects.create(
            title='Título da Palestra',
            start='13:00',
            description='Descrição da palestra.'
        )
        c1 = Course.objects.create(
            title='Título do Curso',
            start='09:00',
            description='Descrição do curso.',
            slots=20
        )

        speaker = Speaker.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            website='http://henriquebastos.net'
        )

        t1.speakers.add(speaker)
        t2.speakers.add(speaker)
        c1.speakers.add(speaker)

        self.resp = self.client.get(r('talk_list'))

    def test_get(self):
        """GET should return status 200."""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use talk_list.html."""
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        """Html must contain information about the talkers."""
        contents = [
            (2, 'Título da Palestra'),
            (1, '10:00'),
            (1, '13:00'),
            (3, '/palestrantes/henrique-bastos/'),
            (3, 'Henrique Bastos'),
            (2, 'Descrição da palestra.'),
            (1, 'Título do Curso'),
            (1, '9:00'),
            (1, 'Descrição do curso.')
        ]

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def test_context(self):
        """Talkers must be in context."""
        variables = ['morning_talks', 'afternoon_talks']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.resp.context)


class TalkListGetEmpty(TestCase):
    """Get empty list of talkers."""

    def setUp(self):
        """Set variables."""

    def test_get_empty(self):
        """GET should return status 200."""
        self.resp = self.client.get(r('talk_list'))
        self.assertContains(self.resp, 'Ainda não existem palestras de manhã.')
        self.assertContains(self.resp, 'Ainda não existem palestras de tarde.')
