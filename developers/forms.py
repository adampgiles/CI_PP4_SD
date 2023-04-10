from django import forms
from .models import Developer, Category, Post

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


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('author', 'publish_date')

    image = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields['title'].label =  'Post Title'
        self.fields['content'].label =  'Post Content'
        self.fields['image'].label =  'Post Image'

        self.fields['title'].required = True
        self.fields['content'].required = True
        self.fields['image'].required = False