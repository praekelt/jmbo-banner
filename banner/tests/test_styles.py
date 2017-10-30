from django.test import TestCase

from banner.styles import BANNER_STYLES_MAP


class BannerStyleTesCase(TestCase):

    def test_custom_styles_can_be_discovered(self):
        self.assertTrue("TestStyle" in BANNER_STYLES_MAP)
