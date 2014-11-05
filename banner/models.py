import re
from random import randint

from django.db import models
from django.core.urlresolvers import reverse

from jmbo.models import ModelBase
from preferences.models import Preferences


class Banner(ModelBase):
    """Legacy base class. Never surfaced in admin."""
    paths = models.TextField(
        null=True,
        blank=True,
        help_text="""A list of regular expressions that match the path. This \
is used to find a banner to render when using a banner proxy. One entry per \
line. If you are unfamiliar with regular expressions then enter the relative \
URL to an item, eg. /post/my-post."""
    )


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

    def get_target_url(self):
        if self.dfp_slot_name and self.dfp_ad_id:
            url = "%s?slot_name=%s&ad_id=%s&url=%s" % \
            (
                reverse('banner-dfp-click-proxy'), self.dfp_slot_name,
                self.dfp_ad_id, self.url
            )
            return url
        return self.url

    @property
    def dfp_tracking_url(self):
        # http://support.google.com/dfp_sb/bin/answer.py?hl=en&answer=1651549
        # tracking pixel section.
        # xxx: I was expecting an ad id but there is none in the example.
        if self.dfp_slot_name:
            url = "http://pubads.g.doubleclick.net/gampad/ad?iu=%s&sz=1x1&t=&c=%s" % \
                (self.dfp_slot_name, randint(0, 2000000000))
        else:
            url = ''
        return url


class ImageBanner(BaseImageBanner):
    pass


class BaseDFPBanner(Banner):
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

    class Meta:
        abstract = True

    @property
    def targeting_values_list(self):
        return self.targeting_values.split('\r\n')


class DFPBanner(BaseDFPBanner):
    pass


class BannerProxy(ModelBase):
    """A banner that inspects the path and renders another banner"""
    banners = models.ManyToManyField(
        Banner,
        blank=True,
        help_text="""A list of banners which are proxied by this item. It is \
useful if a page contains more than one banner proxy."""
    )
    default_banner = models.ForeignKey(
        Banner,
        blank=True,
        null=True,
        related_name='bannerproxy_default_banner'
    )

    class Meta:
        verbose_name_plural = 'Banner proxies'

    def get_actual_banner(self, request):
        """Return first banner matching the path"""

        # Try our set of banners
        request_path = request.get_full_path()
        path_banner_pairs = []
        banners = Banner.permitted.filter(
            id__in=self.banners.all()
        ).order_by('?')
        for banner in banners:
            if banner.paths:
                for path in banner.paths.split():
                    path_banner_pairs.append((path, banner))

        # Sort banner pairs because we want the best regex match
        path_banner_pairs.sort(lambda a, b: cmp(len(b[0]), len(a[0])))

        # Return first match
        for path, banner in path_banner_pairs:
            if re.search(r'%s' % path, request_path):
                return banner.as_leaf_class()

        # Fall back to default banner
        if self.default_banner:
            try:
                default_banner = Banner.permitted.get(id=self.default_banner.id)
                return default_banner.as_leaf_class()
            except Banner.DoesNotExist:
                pass

        return None


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
