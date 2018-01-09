from django.contrib import admin

from jmbo.admin import ImageInline, ModelBaseAdmin

from banner.models import Banner, Button


class ButtonAdminInline(admin.TabularInline):
    model = Banner.buttons.through
    verbose_name = "Button"
    verbose_name_plural = "Buttons"


class BannerAdmin(ModelBaseAdmin):
    inlines = [ImageInline, ButtonAdminInline]


admin.site.register(Banner, BannerAdmin)
admin.site.register(Button)
