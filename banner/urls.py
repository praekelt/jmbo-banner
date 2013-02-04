from django.conf.urls.defaults import patterns, url


urlpatterns = patterns(
    'banner.views',

    # Click proxy. No need for pretty urls.
    url(
        r'^dfp-click-proxy/$', 
        'dfp_click_proxy', 
        {},
        name='banner-dfp-click-proxy'
    ),
)
