from django import forms

class GuestForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Имя')
    email = forms.EmailField(max_length=254, required=True, label='Email')
    text = forms.CharField(max_length=2000, required=True, label='Текст',
                           widget=forms.Textarea)
