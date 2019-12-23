from django import forms
from .models import Team

class TeamCreateForm(forms.ModelForm):

    class Meta:
        fields = ('name', 'description')
        model = Team

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Team Name'
        self.fields['description'].label = 'Team Description'
        # Check out help_text for more