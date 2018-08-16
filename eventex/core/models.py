"""Docstring for the core models."""
from django.db import models
from django.shortcuts import resolve_url as r


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

    class Meta:
        """Set Meta of the Contact."""

        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        """Return value of the speaker's contact in the admin."""
        return self.value
