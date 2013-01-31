from django.db import models

from jmbo.models import ModelBase
from preferences.models import Preferences


class Banner(ModelBase):
    pass


class CodeBanner(Banner):
    code = models.TextField(
        help_text='The full HTML/Javascript code snippet to be \
embedded for this banner.'
    )


class BaseImageBanner(Banner):
    """For every different aspect ratio of image banner a subclass is required.
    Use this class as base."""
    url = models.CharField(
        max_length='256',
        verbose_name='URL',
        help_text='URL (internal or external) to which this banner will link.'
    )

    class Meta:
        abstract = True

    def get_absolute_url(self):
        return self.url


class ImageBanner(BaseImageBanner):
    pass


class DFPBanner(Banner):
    slot_name = models.CharField(
        max_length=256, 
        help_text="An identifier provided by Google, eg. /1234/travel."
    )
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    targeting_key = models.CharField(
        max_length=128, 
        help_text="Eg. 'interests'."
    )
    targeting_values = models.TextField(
        help_text="""Eg. 'sports'. One entry per line. Entries are allowed to \
contain spaces."""
        )

    @property
    def targeting_values_list(self):
        return self.targeting_values.split('\r\n')


class BannerPreferences(Preferences):
    __module__ = 'preferences.models'

    class Meta():
        verbose_name = 'Banner preferences'
        verbose_name_plural = 'Banner preferences'


class BannerOption(models.Model):
    banner_preferences = models.ForeignKey('preferences.BannerPreferences')
    is_default = models.BooleanField(
        verbose_name="Default",
        default=False,
    )
    url_name = models.CharField(
        max_length=256,
        verbose_name="URL Name",
        blank=True,
        null=True,
    )
    url = models.CharField(
        max_length=256,
        verbose_name="URL (takes precedence)",
        blank=True,
        null=True,
    )
    banner = models.ForeignKey('banner.Banner')
    position = models.CharField(max_length=256)
