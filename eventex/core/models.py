"""Docstring for the core models."""
from django.db import models
from django.shortcuts import resolve_url as r

from eventex.core.managers import KindQuerySet, PeriodManager
# ------ more easy way to do this.
# from eventex.core.managers import KindContactManager
# ------ hard way to do this.
# from eventex.core.managers import EmailContactManager, PhoneContactManager


class Speaker(models.Model):
    """Create model speaker."""

    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    photo = models.URLField('foto')
    website = models.URLField('website', blank=True)
    description = models.TextField('descrição', blank=True)

    class Meta:
        """Set Meta of the Speaker."""

        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def __str__(self):
        """Return name of the speaker in the admin."""
        return self.name

    def get_absolute_url(self):
        """Set absolute url to speaker."""
        return r('speaker_detail', slug=self.slug)


class Contact(models.Model):
    """Create model contact."""

    EMAIL = 'E'
    PHONE = 'P'
    KINDS = ((EMAIL, 'Email'),
             (PHONE, 'Telefone'))

    speaker = models.ForeignKey('Speaker', on_delete=models.CASCADE, verbose_name='palestrante')
    kind = models.CharField('tipo', max_length=1, choices=KINDS)
    value = models.CharField('valor', max_length=255)

    objects = KindQuerySet.as_manager()
    # ------ more easy way to do this.
    # objects = KindContactManager()
    # ------ hard way to do this.
    # emails = EmailContactManager()
    # phones = PhoneContactManager()

    class Meta:
        """Set Meta of the Contact."""

        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        """Return value of the speaker's contact in the admin."""
        return self.value


class Talk(models.Model):
    """Create model talk."""

    title = models.CharField('título', max_length=200)
    start = models.TimeField('início', blank=True, null=True)
    description = models.TextField('descrição', blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name='palestrantes', blank=True)

    objects = PeriodManager()

    class Meta:
        """Set Meta of the talk."""

        verbose_name = 'palestra'
        verbose_name_plural = 'palestras'

    def __str__(self):
        """Return name of the talker's title in the admin."""
        return self.title
