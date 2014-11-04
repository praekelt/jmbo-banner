from django import template

from django.contrib.admin import helpers
from django.shortcuts import render_to_response

import object_tools

from banner.forms import Import
from banner.models import DFPBanner


class DFPImport(object_tools.ObjectTool):
    name = 'import'
    label = 'Import'
    help_text = 'Import DFP Banners.'
    form_class = Import

    def import_response(self, form):
        return {}

    def view(self, request, extra_context=None, process_form=True):
        form = extra_context['form']
        if form.is_valid() and process_form:
            return self.export_response(form)

        adminform = helpers.AdminForm(form, form.fieldsets, {})

        context = {'adminform': adminform}
        context.update(extra_context or {})
        context_instance = template.RequestContext(request)

        return render_to_response(
            'banner/import_form.html',
            context,
            context_instance=context_instance
        )

object_tools.tools.register(DFPImport, DFPBanner)
