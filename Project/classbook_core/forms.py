from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# This class uses the built in django UserCreationForm and adds an email field
class SignUpForm(UserCreationForm):
    email = forms.EmailField(initial='@mta.ac.il', help_text='Required. must use an academic email.', required=True)

    class Meta:
        model = User

        # There are 2 password fields to confirm the password (pw1 and pw2 are built-in function names)
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        ACADEMIC_EMAIL_SUFFIX = '@mta.ac.il'
        email = self.cleaned_data['email']

        if not email.endswith(ACADEMIC_EMAIL_SUFFIX):
            raise forms.ValidationError(f'An academic email should end with {ACADEMIC_EMAIL_SUFFIX}')

        return email

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.clean_email()

        if commit:
            user.save()

        return user

