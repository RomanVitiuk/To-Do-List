from .models import Task

from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label='User Name',
        widget=forms.TextInput(
            attrs={
                "type":"text",
                "class":"form-control",
                "id":"form3Example1c",
                # "icon": "bi bi-person-fill",
            }
        )
    )
    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'type':"email",
                'class':"form-control",
                'id':"form3Example3c",
                # "icon": "fas fa-envelope fa-lg me-3 fa-fw",
            }
        )
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "type":"password",
                "id":"form3Example4c",
                "class":"form-control",
                # "icon": "fas fa-lock fa-lg me-3 fa-fw",
            }
        )
    )
    password2 = forms.CharField(
        label="Repeat your password",
        widget=forms.PasswordInput(
            attrs={
                "type":"password",
                "id":"form3Example4c",
                "class":"form-control",
                # "icon": "fas fa-key fa-lg me-3 fa-fw",
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class AddTaskForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                "type":"text",
                "id":"form4Example1",
                "class":"form-control text-center"
            }
        )
    )
    description = forms.CharField(
        label='Task Description',
        widget=forms.Textarea(
            attrs={
                "class":"form-control text-center",
                "id":"form4Example3",
                "rows":"5",
            }
        )
    )

    class Meta:
        model = Task
        fields = ('title', 'description', )


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'is_complete', )
        widgets = {
            'title': forms.TextInput(
                attrs={
                "type":"text",
                "id":"form4Example1",
                "class":"form-control text-center"
            }
            ),
            'description': forms.Textarea(
                attrs={
                "class":"form-control text-center",
                "id":"form4Example3",
                "rows":"5",
            }
            ),
            'is_complete': forms.CheckboxInput(
                attrs={
                    "class":"form-check-input",
                    "type":"checkbox",
                    "id":"form1Example3",
                }
            )
        }
