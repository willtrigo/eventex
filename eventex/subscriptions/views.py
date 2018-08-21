"""Subscriptions views."""
from django.views.generic import DetailView

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.mixins import EmailCreateView
from eventex.subscriptions.models import Subscription


# render subscribe.
new = EmailCreateView.as_view(model=Subscription, form_class=SubscriptionForm, email_subject='Confirmação de inscrição')


# render detail view.
detail = DetailView.as_view(model=Subscription)
