from django import template
from django.contrib.sites.models import Site
from django.test import TestCase

from banner.models import Banner
from banner.styles import BANNER_STYLE_CLASSES


class TemplateTagTestCase(TestCase):
    fixtures = ["sites.json"]

    @classmethod
    def setUpTestData(cls):
        super(TemplateTagTestCase, cls).setUpTestData()
        cls.banner = Banner.objects.create(
            title="Test Banner",
            state="published",
            style=BANNER_STYLE_CLASSES[0].__name__
        )
        cls.banner.sites = list(Site.objects.all())
        cls.banner.publish()

    def test_renders_if_object_is_passed(self):
        # renders if object is passed
        context = template.Context({"banner": self.banner})
        t = template.Template(
            """
            {% load banner_tags %}
            {% render_banner banner %}
            """
        )
        result = t.render(context)
        self.failUnless("Test Banner" in result)

    def test_renders_if_slug_is_passed(self):
        context = template.Context({"banner": self.banner})
        t = template.Template(
            """
            {% load banner_tags %}
            {% render_banner "test-banner" %}
            """
        )
        result = t.render(context)
        self.failUnless("Test Banner" in result)

    def test_raises_exception_if_banner_not_specified(self):
        context = template.Context({"banner": self.banner})
        with self.assertRaisesMessage(
            template.TemplateSyntaxError,
            "render_banner tag requires at the slug or the banner object."
        ):
            template.Template(
                """
                {% load banner_tags %}
                {% render_banner %}
                """
            )