from django import template

register = template.Library()


@register.tag
def get_actual_banner(parser, token):
    """Get actual banner for a BannerProxy object.

    Syntax::

        {% get_actual_banner for [object] as [varname] %}
    """
    tokens = token.contents.split()
    if len(tokens) != 5:
        raise template.TemplateSyntaxError(
            "%r tag requires 4 arguments" % tokens[0]
        )

    if tokens[1] != 'for':
        raise template.TemplateSyntaxError(
            "First argument in %r tag must be 'for'" % tokens[0]
        )

    if tokens[3] != 'as':
        raise template.TemplateSyntaxError(
            "Third argument in %r tag must be 'as'" % tokens[0]
        )

    return ActualBannerNode(obj=tokens[2], as_var=tokens[4])


class ActualBannerNode(template.Node):

    def __init__(self, obj, as_var):
        self.obj = template.Variable(obj)
        self.as_var = template.Variable(as_var)

    def render(self, context):
        obj = self.obj.resolve(context)
        as_var = self.as_var.resolve(context)
        context[as_var] = obj.get_actual_banner(context['request'])
        return ''
