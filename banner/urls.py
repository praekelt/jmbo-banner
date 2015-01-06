from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',

    # Click proxy. No need for pretty urls.
    url(
        r'^dfp-click-proxy/$',
        'banner.views.dfp_click_proxy',
        {},
        name='banner-dfp-click-proxy'
    ),

)
