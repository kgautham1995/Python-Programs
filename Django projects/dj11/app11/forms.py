from django import forms
from app11.models import studentmodel

class studentform(forms.ModelForm):
    class Meta:
        model = studentmodel
        fields = "__all__"