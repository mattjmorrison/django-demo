from django import forms
from sample import models, fields, widgets


class ResultsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ResultsForm, self).__init__(*args, **kwargs)
        queryset = models.Dummy.objects.get_active()
        self.fields['choices'] = fields.DummyChoiceField(queryset, widget=widgets.ImageCheckBoxSelectMultiple)

    class Meta(object):
        model = models.Results
