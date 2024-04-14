

from django import forms
from testapp.models import VoterModel

class VoterForm(forms.Form):
    search_vote=forms.CharField(label='search')