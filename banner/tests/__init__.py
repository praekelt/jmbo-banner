from django.test import TestCase as BaseTestCase
from django.test.client import Client as BaseClient, RequestFactory
from django.contrib.auth.models import User
from django.template import RequestContext, loader

from banner.models import ImageBanner


class TestCase(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = RequestFactory()
        cls.client = BaseClient()

        # Editor
        cls.editor, dc = User.objects.get_or_create(
            username='editor',
            email='editor@test.com'
        )
        cls.editor.set_password("password")
        cls.editor.save()

        # Image banner
        obj, dc = ImageBanner.objects.get_or_create(
            title='ImageBanner',
            owner=cls.editor, state='published',
        )
        obj.sites = [1]
        obj.save()
        cls.imagebanner = obj

    def test_imagebanner_detail(self):
        response = self.client.get(self.imagebanner.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.failUnless(
            """<a href="" rel="nofollow"><img src="" alt="ImageBanner" \
alt="ImageBanner" /></a>""" in response.content
        )

    def test_imagebanner_list_item(self):
        t = loader.get_template(
            "banner/inclusion_tags/imagebanner_list_item.html"
        )
        context = RequestContext(self.request)
        context["object"] = self.imagebanner
        html = t.render(context)
        self.failUnless(
            """<a href="" rel="nofollow"><img src="" alt="ImageBanner" \
alt="ImageBanner" /></a>""" in html
        )
