from django import forms


class SliderForm(forms.Form):
    slider = forms.ChoiceField(widget=forms.CheckboxInput)


class DropdownForm(forms.Form):
    dropdown = forms.ChoiceField(choices=[(x,x) for x in range(1,10)])