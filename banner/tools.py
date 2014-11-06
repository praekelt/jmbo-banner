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


# order is important
DFP_IMPORT_FIELDS = getattr(settings, 'DFP_IMPORT_FIELDS', [
    'title', 'slot_name', 'width', 'height', 'targeting_key',
    'targeting_values', 'paths', 'subtitle'
])


class DFPImport(object_tools.ObjectTool):
    name = 'import'
    label = _('Import')
    help_text = _('Import DFP Banners.')
    form_class = ImportForm

    def save_data(self, data, header_exists):
        """
        Save the data row by row to the database. Title is inferred and all
        sites are selected by default.
        """
        # strip the header if it exists
        data = data if not header_exists else list(data)[1:]

        for row in data:
            # get the entry if it already exists
            try:
                obj = DFPBanner.objects.get(
                    title=row['title'],
                    subtitle=row['subtitle']
                )
            except (DFPBanner.DoesNotExist, KeyError):
                obj = None

            # if the entry doesn't exist, create a new instance
            if not obj:
                obj = DFPBanner()

            # map the fields from the imported csv
            for field in DFP_IMPORT_FIELDS:
                setattr(obj, field, row[field])

            obj.save()

            # add all sites by default - this need to be done after initial save
            # to prevent runtime error related to jmbo.models.ModelBase.__unicode__
            obj.sites = [s for s in Site.objects.all()]
            obj.save()

    def handle_import(self, form):
        csv_file = form.files['csv_file']
        heading_row = csv.reader(csv_file).next()

        # determine if a header row exists
        header_exists = bool([
            field for field in DFP_IMPORT_FIELDS
            if field in [
                header.replace(" ", "_").lower() for header in heading_row
            ]
        ])

        data_dict = csv.DictReader(
            csv_file, fieldnames=DFP_IMPORT_FIELDS
        )

        self.save_data(data_dict, header_exists)

    def view(self, request, extra_context=None, process_form=True):
        form = extra_context['form']

        # valid form and handle the import
        if form.is_valid() and process_form:
            self.handle_import(form)
            message = _('The DFP banners have been successfully imported.')
            messages.add_message(request, messages.SUCCESS, message)

        adminform = helpers.AdminForm(form, form.fieldsets, {})

        context = {'adminform': adminform}
        context.update(extra_context or {})
        context_instance = template.RequestContext(request)

        return render_to_response(
            'admin/banner/import_form.html',
            context,
            context_instance=context_instance
        )

object_tools.tools.register(DFPImport, DFPBanner)
