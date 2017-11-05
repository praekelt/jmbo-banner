from django.test import TestCase

from banner.styles import BANNER_STYLES_MAP, BANNER_STYLE_CLASSES, BaseStyle
from banner.tests.banner_config.styles import TestStyle


class BannerStyleTestCase(TestCase):
    """
    Verify that styles are discoverable and work as expected.
    A 'test style config' is configured to test this at
    banner.tests.banner_config
    """

    def test_custom_styles_can_be_discovered(self):
        self.assertTrue("TestStyle" in BANNER_STYLES_MAP)

    def test_no_duplicate_styles(self):
        # Styles should not be duplicated in the list
        # There should only be two styles in the tests,
        # namely BaseStyle and TestStyle
        print "==============================="
        print BANNER_STYLE_CLASSES
        self.assertEqual(len(BANNER_STYLE_CLASSES), 2)
        self.assertIn(TestStyle, BANNER_STYLE_CLASSES)
        self.assertIn(BaseStyle, BANNER_STYLE_CLASSES)
