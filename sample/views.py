from django import http
from django.views import generic
from sample import models, forms


class Index(generic.CreateView):
    model = models.Dummy
    success_url = '/'


class Picker(generic.CreateView):
    model = models.Results
    form_class = forms.ResultsForm
    success_url = '/'
