from django.contrib import admin
from django.core.urlresolvers import NoReverseMatch

from banner.models import CodeBanner, ImageBanner, DFPBanner, BannerProxy
from jmbo.admin import ModelBaseAdmin


class ImageBannerAdmin(ModelBaseAdmin):

    def _get_absolute_url(self, obj):
        try:
            return super(ImageBannerAdmin, self)._get_absolute_url(obj)
        except NoReverseMatch:
            return "Add banner urls to settings, e.g. <code>(r'^banner/', include('banner.urls'))</code>"

    _get_absolute_url.short_description = 'Permalink'
    _get_absolute_url.allow_tags = True


class DFPBannerAdmin(ModelBaseAdmin):

    def get_fieldsets(self, *args, **kwargs):
        """Re-order fields"""
        result = super(DFPBannerAdmin, self).get_fieldsets(*args, **kwargs)
        result = list(result)
        fields = list(result[0][1]['fields'])
        for name in ('slot_name', 'width', 'height', 'targeting_key',
                     'targeting_values', 'paths'):
            fields.remove(name)
            fields.append(name)
        result[0][1]['fields'] = tuple(fields)

        return tuple(result)


admin.site.register(CodeBanner, ModelBaseAdmin)
admin.site.register(ImageBanner, ImageBannerAdmin)
admin.site.register(DFPBanner, DFPBannerAdmin)
admin.site.register(BannerProxy, ModelBaseAdmin)
