from django import forms
from .models import Developer, Category

class DeveloperProfileForm(forms.ModelForm):

    class Meta:
        model = Developer
        exclude = ('count_sold', 'image_url')

    image = forms.ImageField(label='Image', required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['first_name'].widget.attrs['autofocus'] = True
        self.fields['category'].choices = friendly_names
        self.fields['first_name'].label =  'First Name'
        self.fields['last_name'].label =  'Last Name'
        self.fields['email'].label =  'Email Address'
        self.fields['category'].label =  'Category'
        self.fields['profile_name'].label =  'Profile Name'
        self.fields['description'].label =  'Profile Description'
        self.fields['price'].label =  'Purchase Price'

        self.fields['price'].placeholder =  '5.00'

