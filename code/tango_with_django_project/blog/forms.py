from django import forms
from blog.models import Blog, Category

# Model definition for Blog entry form
class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=100, help_text="Please enter a title:")
    slug = forms.SlugField(max_length=100, help_text="Please enter a slug:")
    body = forms.CharField(widget=forms.Textarea, help_text="Enter the body of your entry:")

    # Inline class to provide additional information on the form
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Blog
        fields = ('title', 'slug', 'body')

class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=100, help_text="Please enter the category name:")
    slug = forms.SlugField(max_length=100, help_text="Please enter the slug name:")

    class Meta:
        model = Category
        fields = ('title', 'slug')
