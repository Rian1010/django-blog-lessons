from django import forms
from .models import Post


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        # No views and dates included in the 'fields' variable, as users cannot edit them
        fields = ('title', 'content', 'image', 'tag', 'published_date')
