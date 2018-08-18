"""Docstring for the core managers."""
from django.db import models


class KindQuerySet(models.QuerySet):
    """Set filter in the query."""

    def emails(self):
        """Set filter email."""
        return self.filter(kind=self.model.EMAIL)

    def phones(self):
        """Set filter phones."""
        return self.filter(kind=self.model.PHONE)

# ------ more easy way to do this.
# class KindContactManager(models.Manager):
#     """Return kind of the filter."""
#
#     def get_queryset(self):
#         """Get query set of the model."""
#         return KindQuerySet(self.model, using=self._db)
#
#     def emails(self):
#         """Must return emails of the contact."""
#         return self.get_queryset().emails()
#
#     def phones(self):
#         """Must return phones of the contact."""
#         return self.get_queryset().phones()

# ------ hard way to do this.
# class EmailContactManager(models.Manager):
#     """Manager email of the contacts."""
#
#     def get_queryset(self):
#         """Set query from contact to get email of the contacts."""
#         qs = super().get_queryset()
#         qs = qs.filter(kind=self.model.EMAIL)
#         return qs
#
#
# class PhoneContactManager(models.Manager):
#     """Manager phone of the contacts."""
#
#     def get_queryset(self):
#         """Set query from contact to get email of the contacts."""
#         qs = super().get_queryset()
#         qs = qs.filter(kind=self.model.PHONE)
#         return qs


class PeriodManager(models.Manager):
    """Set period filter of the times."""

    MIDDAY = '12:00'

    def at_morning(self):
        """Set morning filter of the start time."""
        return self.filter(start__lt=self.MIDDAY)

    def at_afternoon(self):
        """Set morning filter of the start time."""
        return self.filter(start__gte=self.MIDDAY)
