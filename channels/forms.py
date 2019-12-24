from django import forms
from .models import Channel

class ChannelCreateForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = Channel

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Name'].label = 'Channel Name:'
        self.fields['Description'].label = 'Channel Description:'
        self.fields['standup_time'].label = 'Daily Standup starts at:'
        self.fields['standup_time'].placeholder = 'Daily'
        self.fields['standup_time'].help_text = 'Format-> hh:mm:ss (example: 6pm -> 18:00:00)'
        self.fields['standup_duration_minutes'].label = 'Daily standup duration in minutes:'
        # Check out help_text for more