import json

from .models import ContributionPlan
from core.signals import Signal
from django.core.serializers.json import DjangoJSONEncoder
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError

_get_contribution_length_signal_params = ["contribution_plan"]
get_contribution_length_signal = Signal(providing_args=_get_contribution_length_signal_params)


def on_get_contribution_length_signal(sender, **kwargs):
    cp = kwargs["contribution_plan"]
    # check if there is a grace period
    length_contribution = 0
    grace_period = cp.benefit_plan.grace_period
    length_contribution = length_contribution + grace_period
    return length_contribution


get_contribution_length_signal.connect(on_get_contribution_length_signal, dispatch_uid="on_contribution_length")