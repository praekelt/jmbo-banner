from django.db import models
from django.utils.translation import ugettext_lazy as _

from jmbo.models import ModelBase
from link.models import Link
from simplemde.fields import SimpleMDEField

from banner.styles import BANNER_STYLE_CLASSES


class Banner(ModelBase):
    """Base class for all banners"""
    link = models.ForeignKey(
        Link, help_text=_("Link to which this banner should redirect."),
        blank=True, null=True
    )
    style = models.CharField(
        choices=[
            (klass.__name__, klass.__name__)
            for klass in BANNER_STYLE_CLASSES
        ],
        max_length=128, default="BaseStyle"
    )
    headline = SimpleMDEField(null=True, blank=True, help_text=_("The banner's headline."))
    body = SimpleMDEField(null=True, blank=True, help_text=_("The banner's main text content."))


class Button(models.Model):
    """Call to action handling"""
    text = models.CharField(
        max_length=60,
        help_text=_("The text to be displayed as the button label")
    )
    link = models.ForeignKey(
        Link, help_text=_("CTA link for this button"), null=True, blank=True
    )
    banner = models.ManyToManyField(
        to=Banner, related_name="buttons",
        null=True, blank=True, through="ButtonOrder"
    )

    def __unicode__(self):
        return self.text


class ButtonOrder(models.Model):
    banner = models.ForeignKey(Banner)
    button = models.ForeignKey(Button)
    position = models.PositiveIntegerField(default=0)

    class Meta(object):
        ordering = ["position"]
