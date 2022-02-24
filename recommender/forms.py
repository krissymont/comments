from django import forms
from .models import Musicdata

class SearchForm(forms.Form):
    artist = forms.CharField(widget=forms.TextInput(attrs={'size': '50'}))
    from_year = forms.IntegerField(required=False)
    to_year = forms.IntegerField(required=False)

class MusicForm(forms.ModelForm):
	class Meta:
		model = Musicdata
		fields = ["name"]
