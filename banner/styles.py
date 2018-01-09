import inspect

from django.apps import apps
from django.template.loader import render_to_string
from django.utils.module_loading import import_module


class BaseStyle(object):
    template_name = "banner/inclusion_tags/banner_detail.html"

    def __init__(self, banner):
        self.banner = banner

    def get_context_data(self, context):
        context["object"] = self.banner
        return context

    def render(self, context):
        context.push()
        new_context = self.get_context_data(context)
        result = render_to_string(self.template_name, new_context.flatten())
        context.pop()
        return result


BANNER_STYLE_CLASSES = []
BANNER_STYLES_MAP = {}
for klass in [BaseStyle]:
    BANNER_STYLE_CLASSES.append(klass)
    BANNER_STYLES_MAP[klass.__name__] = klass

for app in apps.get_app_configs():
    try:
        mod = import_module("{}.banner_config.{}".format(app.name, "styles"))
    except ImportError:
        pass
    else:
        for name, klass in inspect.getmembers(
            mod,
            lambda o: inspect.isclass(o) and issubclass(o, BaseStyle)
        ):
            if klass not in BANNER_STYLE_CLASSES:
                BANNER_STYLE_CLASSES.append(klass)
                BANNER_STYLES_MAP[klass.__name__] = klass
