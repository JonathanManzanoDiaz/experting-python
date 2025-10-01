from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'slug']
        widgets = {
            "title": forms.TextInput(attrs={"class": "title", "placeholder": "Title"}),
            "body": forms.Textarea(attrs={"class": "body", "placeholder": "Body"}),
            "slug": forms.TextInput(attrs={"class": "slug", "placeholder": "Slug"}),
        }