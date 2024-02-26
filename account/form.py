from django import forms

from account.models import CustomUser


class AccountForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'bio', 'first_name', 'last_name','image']
