import csv

from django import template
from django.conf import settings
from django.contrib import messages
from django.contrib.admin import helpers
from django.contrib.sites.models import Site
from django.shortcuts import render_to_response
from django.utils.translation import ugettext as _

import object_tools

from banner.forms import ImportForm
from banner.models import DFPBanner


DFP_IMPORT_FIELD_MAPPER = getattr(settings, 'DFP_IMPORT_FIELD_MAPPER', {
    'title': 'Title',
    'slot_name': 'Slot Name',
    'width': 'Width',
    'height': 'Height',
    'targeting_key': 'Targeting Key',
    'targeting_values': 'Targeting Value',
    'paths': 'Paths',
    'subtitle': 'Comment'
})


class CSVValidationError(Exception):
    pass


class DFPImport(object_tools.ObjectTool):
    name = 'import'
    label = _('Import')
    help_text = _('Import DFP Banners.')
    form_class = ImportForm

    def save_data(self, data):
        """
        Save the data row by row to the database. Title in infered and all sites
        are selected by default.
        """
        for row in data:

            # get the entry if it already exists
            try:
                title_key = DFP_IMPORT_FIELD_MAPPER['title']
                obj = DFPBanner.objects.get(
                    title=row[title_key]
                )
            except (DFPBanner.DoesNotExist, KeyError):
                obj = None

            # if the entry doesn't exist, create a new instance
            if not obj:
                obj = DFPBanner()

            # map the fields from the imported csv
            for key, value in DFP_IMPORT_FIELD_MAPPER.items():
                setattr(obj, key, row[value])

            obj.sites = [s.pk for s in Site.objects.all()]
            obj.save()

    def validate(self, form):
        csv_file = form.files['csv_file']
        heading_row = csv.reader(csv_file).next()

        # validate the import files columns
        for field in DFP_IMPORT_FIELD_MAPPER.values():
            if field.lower() not in [row.lower() for row in heading_row]:
                raise CSVValidationError(
                    _("Field missing from csv: %s" % field)
                )

        self.save_data(csv.DictReader(csv_file))

    def view(self, request, extra_context=None, process_form=True):
        form = extra_context['form']
        if form.is_valid() and process_form:
            self.validate(form)
            message = _('The DFP banners have been successfully imported.')
            messages.add_message(request, messages.SUCCESS, message)

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
