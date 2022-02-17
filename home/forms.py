from django import forms
from ckeditor.widgets import CKEditorWidget
from django.db.models import fields
from .models import PastedText


class PastedTextForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(),
                             label="Paste your text below")
    password = forms.CharField(max_length=200,label="Password(Enter paster for everyone to access)")
    class Meta:
        model = PastedText
        fields = ['text','password']
