
from .models import Tasks
from django import forms
from django.utils import timezone


class todoform(forms.ModelForm):
    class Meta:
        model=Tasks
        fields='__all__'
    def clean(self):
        data=self.cleaned_data['completiondate']
        if data<=timezone.now():
            raise forms.ValidationError({'completiondate':'completion date can not be in future'})
        
          