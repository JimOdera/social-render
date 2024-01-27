from django import forms
from app.models import Post, Profile

from django.contrib.auth.models import User


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'status')


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(
        attrs={'placeholder': 'Enter your username...'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter your Password...'}))


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter your Password...'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm your Password...'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        help_texts = {
            'username': None,
            'email': None,
        }

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Password Missmatch')
        return confirm_password


class UserEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'readonly': 'readonly'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'readonly': 'readonly'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

        widgets = {
            'bio': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Share Something about yourself...'
            }),
        }
