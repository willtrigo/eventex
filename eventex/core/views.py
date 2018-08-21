"""Docstring core views."""
from django.views.generic import ListView, DetailView

from eventex.core.models import Speaker, Talk


# Render home.
home = ListView.as_view(template_name='index.html', model=Speaker)


# Render speaker detail.
speaker_detail = DetailView.as_view(model=Speaker)


# Render talk list.
talk_list = ListView.as_view(model=Talk)
