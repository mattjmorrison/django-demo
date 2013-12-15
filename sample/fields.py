from django.forms import ModelMultipleChoiceField
from django.conf import settings
from django.utils.safestring import mark_safe
from sample.widgets import ImageCheckBoxSelectMultiple


class DummyChoiceField(ModelMultipleChoiceField):

    def label_from_instance(self, obj):
        return mark_safe("""
          Something Here: <img src="{}{}" style="height: 200px; width: 300px;" />
        """.format(settings.MEDIA_URL, obj.image))
