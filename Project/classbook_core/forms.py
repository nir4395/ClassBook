from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# TODO: get Institution choices from the DB instead and add more choices
ACADEMIC_INSTITUTION_CHOICES = (
    ("1", "Tel Aviv University"),
    ("2", "Technion"),
    ("3", "Academic College of Tel Aviv Yafo"),
)

# This class uses the built in django UserCreationForm and adds an email field
class SignUpForm(UserCreationForm):
    email = forms.EmailField(initial='@accademic_email_suffix', help_text='Required. must use an academic email.', required=True)
    Institution = forms.MultipleChoiceField(choices = ACADEMIC_INSTITUTION_CHOICES)

    class Meta:
        model = User

        # There are 2 password fields to confirm the password (pw1 and pw2 are built-in function names)
        fields = ("username", "password1", "password2", "Institution", "email")

    def clean_email(self):
        # TODO: changes this to check the correct instituation email
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

