"""Docstring core views."""
from django.shortcuts import render, get_object_or_404

from eventex.core.models import Speaker


def home(request):
    """Render home."""
    speakers = Speaker.objects.all()
    return render(request, 'index.html', {'speakers': speakers})


def speaker_detail(request, slug):
    """Render speaker."""
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'core/speaker_detail.html', {'speaker': speaker})
