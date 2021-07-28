from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
# from classbook_core.models import Institution

# TODO:
# we currently have a bug which does not allow us to use Institution.get_accademic_instituion_choices() in the form below
# because of this bug - we use <supported_institutions> global variable instead
supported_institutions = [
    (0, 'Academic College of TLV        '),
    (1, 'TLV University                 '),
    (2, 'Technion                       '),
    (3, 'University Of Haifa            '),
    (4, 'Bar Ilan University            '),
    (5, 'Ariel University               '),
    (6, 'Hebrew University of Jersulam  '),
    (7, 'IDC Harezlia                   '),
    (8, 'Afeka College                  '),
    (9, 'HIT                            '),
    (10, 'Shenkar College               '),
    (11, 'Sami Shamoon College          '),
]

# This class uses the built in django UserCreationForm and adds an email field
class SignUpForm(UserCreationForm):
    email = forms.EmailField(initial='@accademic_email_suffix', help_text='Required. must use an academic email.', required=True)
    institution = forms.ChoiceField(
        # TODO: dynamicly change the email field of the form based on the JS function updateAccademicEmail()
        widget=forms.Select(attrs = {'onchange' : "updateAccademicEmail();"}),
        choices=supported_institutions
    )

    class Meta:
        model = User

        # There are 2 password fields to confirm the password (pw1 and pw2 are built-in function names)
        fields = ("username", "password1", "password2", "institution", "email")


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
