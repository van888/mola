from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True,help_text="Email field is required.")
    firstname = forms.CharField(max_length=50, required=False, help_text="Optional. Can fill in later.")
    lastname = forms.CharField(max_length=50, required=False, help_text="Optional. Can fill in later.")

    class Meta:
        model = User
        fields = ('firstname',
                  'lastname',
                  'username',
                  'email',
                  'password1',
                  'password2')

        def save(self, commit=True):
            user = super(UserCreationForm, self).save(commit=False)
            user.email = self.cleaned_data["email"]
            user.firstname = self.cleaned_data["firstname"]
            user.lastname = self.cleaned_data["lastname"]
            if commit:
                user.save()
            return user