import threading
import urllib2

from django.http import HttpResponseRedirect


class WgetThread(threading.Thread):

    def __init__(self, url):
        super(WgetThread, self).__init__()
        self.url = url

    def run(self):
        result = urllib2.urlopen(self.url).read()


def dfp_click_proxy(request):
    """Fire off an asynch request and redirect to image banner target"""
    url = "http://pubads.g.doubleclick.net/gampad/clk?iu=%s&id=%s" % \
        (request.GET['slot_name'], request.GET['ad_id'])
    t = WgetThread(url)
    t.start()
    return HttpResponseRedirect(request.GET['url'])
