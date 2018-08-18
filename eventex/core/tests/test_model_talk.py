"""Docstring models for talkers."""
from django.test import TestCase

from eventex.core.managers import PeriodManager
from eventex.core.models import Talk, Course


class TalkModelTest(TestCase):
    """Test models of the talks."""

    def setUp(self):
        """Set variables."""
        self.talk = Talk.objects.create(
            title='Título da Palestra',
            start='10:00',
            description='Descrição da palestra.'
        )

    def test_create(self):
        """Test create model talk."""
        self.assertTrue(Talk.objects.exists())

    def test_has_speakers(self):
        """Talk has many Speakers and vice-versa."""
        self.talk.speakers.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            website='http://henriquebastos.net'
        )
        self.assertEqual(1, self.talk.speakers.count())

    def test_description_can_be_blank(self):
        """Validate attribute of description field to be equal true."""
        field = Talk._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_speakers_can_be_blank(self):
        """Validate attribute of speakers field to be equal true."""
        field = Talk._meta.get_field('speakers')
        self.assertTrue(field.blank)

    def test_start_can_be_blank(self):
        """Validate attribute of start field to be equal true."""
        field = Talk._meta.get_field('start')
        self.assertTrue(field.blank)

    def test_start_can_be_null(self):
        """Validate attribute of start field to be equal true."""
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)

    def test_str(self):
        """Validate str."""
        self.assertEqual('Título da Palestra', str(self.talk))


class PeriodManagerTest(TestCase):
    """Test manager of the time in talks."""

    def setUp(self):
        """Set variables."""
        Talk.objects.create(title='Morning Talk', start='11:59')
        Talk.objects.create(title='Afternoon Talk', start='12:00')

    def test_manager(self):
        """Test manager period."""
        self.assertIsInstance(Talk.objects, PeriodManager)

    def test_at_morning(self):
        """Validate query to find morning periods of the talk."""
        qs = Talk.objects.at_morning()
        expected = ['Morning Talk']
        self.assertQuerysetEqual(qs, expected, lambda o: o.title)

    def test_at_afternoon(self):
        """Validate query to find afternoon periods of the talk."""
        qs = Talk.objects.at_afternoon()
        expected = ['Afternoon Talk']
        self.assertQuerysetEqual(qs, expected, lambda o: o.title)


class CourseModelTest(TestCase):
    """Test models of the courses."""

    def setUp(self):
        """Set variables."""
        self.course = Course.objects.create(
            title='Título do Curso',
            start='09:00',
            description='Descrição do curso.',
            slots=20
        )

    def test_create(self):
        """Test create model course."""
        self.assertTrue(Course.objects.exists())

    def test_speakers(self):
        """Course has many speakers and vice-versa."""
        self.course.speakers.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            website='http://henriquebastos.net'
        )
        self.assertEqual(1, self.course.speakers.count())

    def test_str(self):
        """Validate str."""
        self.assertEqual('Título do Curso', str(self.course))

    def test_manager(self):
        """Validate period of the course."""
        self.assertIsInstance(Course.objects, PeriodManager)
