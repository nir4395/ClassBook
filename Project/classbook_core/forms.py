from classbook_core.models import Institution
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import widgets
from django.db.utils import OperationalError
import logging



# This class uses the built in django UserCreationForm and adds an email field
class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(help_text='Required. must use an academic email.', required=True)

    try:
        institution = forms.ChoiceField(
            # TODO: dynamically change the email field of the form based on the JS function updateAccademicEmail()
            widget=forms.Select(attrs = {'onchange' : "updateAcademicEmail();"}),
            # choices=supported_institutions
            choices=Institution.get_academic_instituion_choices()
        )
    except OperationalError:
        logging.debug('Trying to fill institutions in signup form before migrations')
        institution = forms.ChoiceField()

    #######################################################

    class Meta:
        model = User
        # There are 2 password fields to confirm the password (pw1 and pw2 are built-in function names)
        fields = ("username", "password1", "password2", "institution", "email")



    # django username field is case sensitive, we override it here in the signup form (save all usersnames in lowercase)
    def clean_username(self):
        cur_username = self.cleaned_data['username'].lower()

        if User.objects.filter(username=cur_username).exists():
            raise forms.ValidationError('User already exists with this username')
        else:
            return cur_username


    # after the form is submitted - check that the email matches the academic institutation
    def clean_email(self):
        email = self.cleaned_data['email']
        institution_id = self.cleaned_data['institution']

        # get the instution name from the list of tuples (supported_institutions) using the instution id we get from the form
        institution = Institution.objects.get(pk=institution_id)
        
        if not email.endswith(institution.academic_email_suffix):
            raise forms.ValidationError(f'{institution.name} email addresses must end with {institution.academic_email_suffix}')

        return email


    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.clean_email()
        
        if commit:
            user.save()

        return user


class SignInForm(AuthenticationForm):

    # django username field is case sensitive, we override it here in the signInForm (login all usersnames with lowercase)
    def clean_username(self):
        return self.cleaned_data['username'].lower