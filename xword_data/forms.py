from django import forms

class DrillForm(forms.Form):
    """A form that allows users to try a guess."""
    answer = forms.CharField(max_length=50)