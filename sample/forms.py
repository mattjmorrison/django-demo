from django import forms
from sample import models, widgets


class ResultsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ResultsForm, self).__init__(*args, **kwargs)
        self.fields['choices'].queryset = models.Dummy.objects.get_active()

    class Meta(object):
        model = models.Results
        widgets = {
            'choices': widgets.ImageCheckBoxSelectMultiple(),
        }
