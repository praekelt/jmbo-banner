from django.conf.urls import include, url


urlpatterns = [
    url(r'^jmbo/', include('jmbo.urls')),
    url(r'^comments/', include('django_comments.urls')),
    # (r'^banner/', include('banner.urls')),
]
