from .models import Client
from django.forms import ModelForm, TextInput, Textarea


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ["FIO", "address", "number_phone", "email", "gender", "policyStatus", "insuranceType", "insuranceAmount", "startDate", "endDate", "premium"]
        widgets = {
            "FIO": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ФИО'
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес'
            }),
            "number_phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер телефона'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите email'
            }),
            "gender": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пол'
            }),
            "policyStatus": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите статус полиса'
            }),
            "insuranceType": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите тип страхования'
            }),
            "insuranceAmount": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите сумму страхования'
            }),
            "startDate": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату начала страхования'
            }),
            "endDate": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату окончания страхования'
            }),
            "premium": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите сумму выплаты клиентом'
            }),
        }