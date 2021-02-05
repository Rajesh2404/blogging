from django import forms
from blogNcode.models import writeBlog

class BlogForm(forms.ModelForm):
    class Meta:
        model = writeBlog
        fields = ['name', 'title', 'blog']

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-style', 'autocomplete': 'off', 'required': '', 'placeholder': 'Name'}),
            'title' : forms.TextInput(attrs={'class': 'form-style', 'autocomplete': 'off', 'required': '', 'placeholder': 'Title'}),
            'blog' : forms.Textarea(attrs={'class': 'form-style', 'rows': '4', 'autocomplete': 'off', 'required': '', 'placeholder': 'Write your thought...'})
        }
