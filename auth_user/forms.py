from django import forms
from .models import User


class UserEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
        widgets = {"email": forms.EmailInput(attrs={
            "class": "form-control",
            "id": "floatingInput",
            "type": "email",
            "label": "Введите данные"
        })}


class UserCodeForm(forms.Form):
    code = forms.CharField(label='Введите код',
                           widget=forms.TextInput(attrs={
                               "class": "form-control",
                               "id": "floatingInput",
                               "type": "code"
                           }))
