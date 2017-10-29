from django.contrib import admin

from jmbo.admin import ImageInline, ModelBaseAdmin

from banner.forms import BannerAdminForm
from banner.models import Banner, Button, ButtonOrder


class ButtonInline(admin.TabularInline):
    model = ButtonOrder
    verbose_name = "Button"
    verbose_name_plural = "Buttons"


class BannerAdmin(ModelBaseAdmin):
    form = BannerAdminForm
    inlines = [ImageInline, ButtonInline]


admin.site.register(Banner, BannerAdmin)
admin.site.register(Button)
