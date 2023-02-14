from django import forms
from .models import Reservation, ContactUs


class ReservationForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'name',
        'class': 'form-control',
        'id': 'name',
        'placeholder': "Ваше ім'я",
        'data-rule': 'minlen:4',
        'data-msg': 'Please enter at least 4 chars'
    }))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'name': 'phone',
        'id': 'phone',
        'placeholder': 'Ваш телефон',
        'data-rule': 'minlen:4',
        'data-msg': 'Please enter at least 4 chars'
    }))
    persons = forms.IntegerField(widget=forms.NumberInput(attrs={
        'type': "number",
        'class': "form-control",
        'name': "people",
        'id': "people",
        'placeholder': "# кількість гостей",
        'data-rule': "minlen:1",
        'data-msg': "Please enter at least 1 chars"
    }))
    message = forms.CharField(max_length=250, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'name': 'message',
        'rows': '5',
        'placeholder': 'Повідомлення'
    }))



    class Meta:
        model = Reservation
        fields = ['name', 'phone', 'persons', 'message']


class ContactUsForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
    'type': "text",
    'name': "name",
    'class': "form-control",
    'id': "name",
    'placeholder': "Вкажіть ваше ім'я"
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'type': "email",
        'class': "form-control",
        'name': "email",
        'id': "email",
        'placeholder': "Вкажіть вашу пошту"
    }))

    subject_mes = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'type': "text",
        'class': "form-control",
        'name': "subject",
        'id': "subject",
        'placeholder': "Тема"
    }))

    message = forms.CharField(max_length=250, widget=forms.Textarea(attrs={
        'class': "form-control",
        'name': "message",
        'rows': "5",
        'placeholder': "Повідомлення"
    }))
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject_mes', 'message']