from django import forms
from .models import Part


class PartEntryForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ('length',
                  'length_band',
                  'width',
                  'width_band',
                  'quantity',
                  'band',
                  'rotation',
                  'panel',
                  'project')
    # def save(self):
    #     cd = self.cleaned_data
