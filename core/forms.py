from django import forms
from django.db.models import fields
from .models import upload_as

class upload_form(forms.ModelForm):
    pdf = forms.FileField()    # class Meta:
    #     model = upload_as
    #     fields ="__all__"