__author__ = 'biceps'

from django import forms
from django.utils.translation import ugettext as _


class FoodStepForm(forms.Form):
    name = forms.CharField(label=_("Ingridient name:"), max_length=256)
    unit = forms.CharField(label=_("Unit:"), max_length=256)
    qty = forms.CharField(label=_("Unit:"), max_length=256)
    comment = forms.CharField(label=_("Comment:"), max_length=256)

