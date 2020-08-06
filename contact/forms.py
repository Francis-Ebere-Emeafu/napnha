from django import forms

from contact.models import ContactMessage


class ContactForm(forms.ModelForm):
    send_copy = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'form-control1', 'placeholder': 'Get message copy'}))

    class Meta:
        model = ContactMessage
        fields = ['title', 'email', 'content']
