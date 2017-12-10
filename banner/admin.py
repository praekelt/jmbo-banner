from django.contrib import admin

from jmbo.admin import ImageInline, ModelBaseAdmin

from banner.models import Banner, Button


class BannerAdmin(ModelBaseAdmin):
    inlines = [ImageInline, ]


admin.site.register(Banner, BannerAdmin)
admin.site.register(Button)
