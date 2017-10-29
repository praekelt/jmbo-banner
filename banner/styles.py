import inspect

from django.apps import apps
from django.template.loader import render_to_string
from django.utils.module_loading import import_module


class AbstractBaseStyle(object):
    image_path = "/admin/banner/images/unknown.png"
    template_name = "banner/inclusion_tags/banner_detail.html"

    # def get_context_data(self, context):
    #     return context

    def render(self, context):
        # context.push()
        # new_context = self.get_context_data(context)
        result = render_to_string(self.template_name, context.flatten())
        # context.pop()
        return result


class Standard(AbstractBaseStyle):
    pass


BANNER_STYLE_CLASSES = []
BANNER_STYLES_MAP = {}
for app in apps.get_app_configs():
    try:
        mod = import_module("{}.banner_config.{}".format(app.name, "styles"))
    except ImportError:
        pass
    else:
        for name, klass in inspect.getmembers(
            mod,
            lambda o: inspect.isclass(o) and issubclass(o, AbstractBaseStyle)
        ):
            BANNER_STYLE_CLASSES.append(klass)
            BANNER_STYLES_MAP[klass.__name__] = klass
