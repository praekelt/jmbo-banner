from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from jmbo.admin import ModelBaseAdminForm

from banner.styles import BANNER_STYLE_CLASSES


class BannerAdminForm(ModelBaseAdminForm):

    def __init__(self, *args, **kwargs):
        super(BannerAdminForm, self).__init__(*args, **kwargs)

        # Custom the style field layout
        choices = []
        self.fields["style"].widget = forms.widgets.RadioSelect()
        for klass in BANNER_STYLE_CLASSES:
            image_path = getattr(klass, "image_path", None)
            image_markup = ""
            if image_path:
                image_markup = \
                    "<img src=\"%s%s\" style=\"max-width: 128px;\" />" \
                    % (settings.STATIC_URL.rstrip("/"), image_path)
            choices.append((
                klass.__name__,
                mark_safe("%s%s" % (image_markup, klass.__name__))
            ))
        self.fields["style"].widget.choices = choices
