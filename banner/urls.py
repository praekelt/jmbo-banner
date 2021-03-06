from django.conf.urls import url

from banner.views import BannerDetailView, BannerListView


app_name = "banner"
urlpatterns = [
    url(
        r"^detail/(?P<slug>[\w-]+)/$",
        BannerDetailView.as_view(),
        name="banner-detail"
    ),
    url(
        r"^$",
        BannerListView.as_view(),
        name="banner-list"
    ),
]
