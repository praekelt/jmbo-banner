from django import forms
from django.utils.translation import ugettext as _


class ImportForm(forms.Form):
    csv_file = forms.FileField(
        required=True,
        label=_('CSV File'),
        help_text=_('CSV File containing import data.')
    )

    def __init__(self, model, *args, **kwargs):
        super(ImportForm, self).__init__(*args, **kwargs)
        self.fieldsets = (
            (_('Import'), {'fields': ('csv_file', )}),
        )
