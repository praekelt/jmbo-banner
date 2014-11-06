from django.http import HttpResponseRedirect

from banner.tasks import dfp_click_proxy_task


def dfp_click_proxy(request):
    """Fire off an async request and redirect to image banner target"""
    dfp_click_proxy_task.delay(request)
    return HttpResponseRedirect(request.GET['url'])
