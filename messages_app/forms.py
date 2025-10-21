from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Type a message...',
                'class': 'w-full p-2 border rounded-lg bg-gray-800 text-white'
            }),
        }
