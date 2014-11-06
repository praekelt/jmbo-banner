import urllib2

from celery import task


@task
def dfp_click_proxy_task(request):
    """Fire off an async request and redirect to image banner target"""
    url = "http://pubads.g.doubleclick.net/gampad/clk?iu=%s&id=%s" % (
        request.GET['slot_name'], request.GET['ad_id']
    )
    return urllib2.urlopen(url).read()
