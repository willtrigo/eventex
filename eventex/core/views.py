"""Docstring core views."""
from django.shortcuts import render


def home(request):
    """Render home."""
    speakers = [{'name': 'Grace Hopper', 'photo': 'http://hbn.link/hopper-pic'},
                {'name': 'Alan Turing', 'photo': 'http://hbn.link/turing-pic'}]
    return render(request, 'index.html', {'speakers': speakers})
