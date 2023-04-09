from django import forms
from .models import Developer, Category

class DeveloperProfileForm(forms.ModelForm):

    class Meta:
        model = Developer
        exclude = ('user', 'count_sold', 'image_url')

    image = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['profile_name'].widget.attrs['autofocus'] = True
        self.fields['category'].choices = friendly_names
        self.fields['profile_name'].label =  'Profile Name'
        self.fields['description'].label =  'Profile Description'
        self.fields['category'].label =  'Category'
        self.fields['price'].label =  'Purchase Price'
        self.fields['price'].placeholder =  '5.00'

        self.fields['category'].required = True
        self.fields['profile_name'].required = True
        self.fields['description'].required = True
        self.fields['category'].required = True
        self.fields['price'].required = True
        self.fields['image'].required = True

