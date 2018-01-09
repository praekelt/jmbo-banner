from jmbo.views import ObjectDetail, ObjectList

from banner.models import Banner


class BannerDetailView(ObjectDetail):
    model = Banner
    template_name = "banner/banner_detail.html"


class BannerListView(ObjectList):
    model = Banner
    template_name = "banner/banner_list.html"
