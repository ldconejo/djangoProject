from django import forms
from blog.models import Blog, Category

# Model definition for Blog entry form
class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    slug = forms.SlugField(max_length=100)
    body = forms.CharField()

    # Inline class to provide additional information on the form
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Blog
        fields = ('title', 'slug', 'body')

class CategoryForm:
    title = forms.CharField(max_length=100)
    slug = forms.SlugField(max_length=100)

    class Meta:
        model = Category
        fields = ('title', 'slug')
