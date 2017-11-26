from jmbo.views import ObjectDetail, ObjectList

from banner.models import Banner


class BannerDetailView(ObjectDetail):
    model = Banner
    template_name = "banner/banner_detail.html"

    def get_template_names(self):
        template_names = [self.template_name]
        other_names = super(BannerDetailView, self).get_template_names()
        template_names.extend(other_names)


class BannerListView(ObjectList):
    model = Banner
    template_name = "banner/banner_list.html"
