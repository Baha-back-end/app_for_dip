from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Product, Profile, Comment


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title',
                  'description',
                  'image',
                  'category')
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название товара"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Характеристики товара"
            }),
            "image": forms.FileInput(attrs={
                "class": "form-control"
            }),
            "category": forms.Select(attrs={
                "class": "form-control"
            })
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Username...'
                               }))
    password = forms.CharField(label="Ваш пароль",
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Password...'
                               }))


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Username...'
                               }))
    first_name = forms.CharField(label="Ваше имя",
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Firstname...'
                                 }))

    Last_name = forms.CharField(label="Ваше фамилия",
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Lastname...'
                                }))
    email = forms.EmailField(label="Ваша почта",
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Email'
                             }))
    password1 = forms.CharField(label="Придумайте пароль",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Password...'
                                }))
    password2 = forms.CharField(label="Подтвердите пароль",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Password...'
                                }))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'mobile', 'address',
                  'job', 'image')

        widgets = {
            'phone': forms.TextInput(attrs={
                "class": "form-control",
                'placeholder': 'Номер телефона'
            }),
            'mobile': forms.TextInput(attrs={
                "class": "form-control",
                'placeholder': 'Номер телефона'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            }),
            'job': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Профессия'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }

class UserForm(forms.ModelForm):
    username = forms.CharField(label="Имя пользователя",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Username...'
                               }))
    first_name = forms.CharField(label="Ваше имя",
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'First Name'
                                 }))

    last_name = forms.CharField(label="Ваша фамилия",
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Last Name'
                                }))
    email = forms.EmailField(label="Ваша почта",
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Email'
                             }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Напишите отзыв к товару!",
                "rows": 5
            })
        }

