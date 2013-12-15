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

    def render(self):
        id_ = self.attrs.get('id', None)
        start_tag = format_html('<ul id="{0}">', id_) if id_ else '<ul>'
        output = [start_tag]
        for widget in self:
            output.append(format_html('<li>{0}</li>', mark_safe(widget)))
        output.append('</ul>')
        return mark_safe('\n'.join(output))


class ImageCheckBoxSelectMultiple(forms.CheckboxSelectMultiple):
    renderer = ImageCheckBoxSelectMultipleRenderer
