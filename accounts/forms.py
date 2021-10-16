from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={
            'name': 'username',
            'id': 'id_username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'name': 'password',
            'id': 'id_password'
        }
    ))


class SignupForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "Kiritgan parollaringiz bir xil emas!",
    }

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )
        error_messages = {
            'username': {
                'unique': 'Bunday foydalanuvchi nomi allaqachon mavjud!',
            },
        }

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        
        self.fields['first_name'].widget.attrs.update({
            'required': True,
        })
        self.fields['last_name'].widget.attrs.update({
            'required': True,
        })
        
        self.fields['username'].label = 'Foydalanuvchi nomi:'
        self.fields['first_name'].label = 'Ism:'
        self.fields['last_name'].label = 'Familiya:'
        self.fields['password1'].label = 'Parol:'
        self.fields['password2'].label = 'Takroriy parol:'
