from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

User = get_user_model()

class UserLoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    def clean(self, *args, **kwargs): # Валидация
        email = self.cleaned_data.get('email').strip()
        password = self.cleaned_data.get('password')

        if email and password:
            qs = User.objects.filter(email=email)
            if not qs.exists:
                raise forms.ValidationError("Пользователь не найден!")
            if not check_password(password, qs[0].password): # равен ли пароль полученный в фильтре
                raise forms.ValidationError("Пароль неверный!")

            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("Данный аккаунт отключен!")

            return super(UserLoginForm, self).clean(*args, **kwargs)



