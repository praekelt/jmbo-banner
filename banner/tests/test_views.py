from django.contrib.sites.models import Site
from django.test import TestCase
from django.urls import reverse

from banner.models import Banner


class DetailViewTestCase(TestCase):
    fixtures = ["sites.json"]

    @classmethod
    def setUpTestData(cls):
        super(DetailViewTestCase, cls).setUpTestData()
        cls.banner = Banner.objects.create(title="Test Banner", style="BaseStyle")
        cls.banner.sites = Site.objects.all()
        cls.banner.publish()

    def test_view_renders(self):
        response = self.client.get(
            reverse("banner:banner-detail", args=[self.banner.slug])
        )
        self.assertEqual(response.status_code, 200)
