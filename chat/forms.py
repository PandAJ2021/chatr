from django import forms 
from .models import ChatRoom

class CreateChatForm(forms.Form):
    name = forms.CharField(max_length=255, label='Chat Room Name')

    def clean_name(self):
        room_name = self.cleaned_data.get('name')
        if not room_name:
            raise forms.ValidationError('This field is required.')
        if ChatRoom.objects.filter(name=room_name).exists():
            raise forms.ValidationError('This room already exists.')
        return room_name