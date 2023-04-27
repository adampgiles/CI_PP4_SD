from django import forms
from .models import ContactUs


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ('user', 'sent_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['subject'].widget.attrs['autofocus'] = True
        self.fields['subject'].label = 'Subject'
        self.fields['body'].label = 'Body'

        self.fields['subject'].required = True
        self.fields['body'].required = False
