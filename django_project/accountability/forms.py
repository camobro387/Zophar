from django import forms

class BibleForm(forms.Form):
    slider = forms.ChoiceField(widget=forms.CheckboxInput)