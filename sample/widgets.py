from django import forms
from django.forms import widgets
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class ImageCheckboxChoiceInput(widgets.CheckboxChoiceInput):

    def __init__(self, *args, **kwargs):
        super(ImageCheckboxChoiceInput, self).__init__(*args, **kwargs)
        self.choice_label = mark_safe(self.choice_label)


class ImageCheckBoxSelectMultipleRenderer(widgets.CheckboxFieldRenderer):
    choice_input_class = ImageCheckboxChoiceInput


class ImageCheckBoxSelectMultiple(forms.CheckboxSelectMultiple):
    renderer = ImageCheckBoxSelectMultipleRenderer
