from django import forms


class Import(forms.Form):
    csv_file = forms.FileField(
        required=True,
        label='CSV File',
        help_text='CSV File containing import data.'
    )

    def __init__(self, model, *args, **kwargs):
        super(Import, self).__init__(*args, **kwargs)
        self.fieldsets = (
            ('Import', {'fields': ('csv_file', )}),
        )
