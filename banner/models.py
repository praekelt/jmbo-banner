from random import randint

from django.db import models
from django.core.urlresolvers import reverse

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
    dfp_tracking_url = models.CharField(
        max_length=256, 
        blank=True, 
        null=True, 
        help_text="An optional URL to track impressions of this banner."
    )
    dfp_slot_name = models.CharField(
        max_length=256, 
        null=True,
        blank=True,
        help_text="""A combination of network code and ad unit as provided \
by Google, eg. /1234/travel. Used to track clicks."""
    )
    dfp_ad_id = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text="The advertisement id. Used to track clicks."
    )

    class Meta:
        abstract = True

    def get_absolute_url(self):
        if self.dfp_slot_name and self.dfp_ad_id:
            url = "%s?slot_name=%s&ad_id=%s&url=%s" % \
            (
                reverse('banner-dfp-click-proxy'), self.dfp_slot_name, 
                self.dfp_ad_id, self.url
            )
            return url
        return self.url

    @property
    def dfp_tracking_url_nocache(self):
        # Add a random parameter to the url to prevent caching
        url = self.dfp_tracking_url
        if not url:
            return ''
        rand_id = str(randint(0, 2000000000))
        if url.find('?') != -1:            
            return url + '&rnd=' + rand_id
        else:
            return url + '?rnd=' + rand_id


class ImageBanner(BaseImageBanner):
    pass


class DFPBanner(Banner):
    slot_name = models.CharField(
        max_length=256, 
        help_text="""A combination of network code and ad unit as provided \
by Google, eg. /1234/travel."""
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
