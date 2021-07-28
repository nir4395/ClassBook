from classbook_core.models import Institution
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
# from classbook_core.models import Institution

# TODO:
# we currently have a bug which does not allow us to use Institution.get_accademic_instituion_choices() in the form below
# because of this bug - we use <supported_institutions> global variable instead
supported_institutions = [
    ('0', 'Academic College of TLV'),
    ('1', 'TLV University'),
    ('2', 'Technion'),
    ('3', 'University Of Haifa'),
    ('4', 'Bar Ilan University'),
    ('5', 'Ariel University'),
    ('6', 'Hebrew University of Jersulam'),
    ('7', 'IDC Harezlia'),
    ('8', 'Afeka College'),
    ('9', 'HIT'),
    ('10', 'Shenkar College'),
    ('11', 'Sami Shamoon College'),
]

# This class uses the built in django UserCreationForm and adds an email field
class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text='Required. must use an academic email.', required=True)
    institution = forms.ChoiceField(
        # TODO: dynamicly change the email field of the form based on the JS function updateAccademicEmail()
        widget=forms.Select(attrs = {'onchange' : "updateAccademicEmail();"}),
        choices=supported_institutions
    )

    class Meta:
        model = User

        # There are 2 password fields to confirm the password (pw1 and pw2 are built-in function names)
        fields = ("username", "password1", "password2", "institution", "email")


    # django username field is not case sensitive, we override it here in the signupform
    def clean_username(self):
        username = self.cleaned_data['username'].lower

        if User.objects.filter(username=username).exists:
            raise forms.ValidationError('User already exists with this username')
        else:
            return username

    # after the form is submited - check that the email matches the accademic institutation
    def clean_email(self):
        email = self.cleaned_data['email']
        institution_id = self.cleaned_data['institution']

        # get the instution name from the list of tuples (supported_institutions) using the instution id we get from the form
        for id_instution_pair in supported_institutions:
            if id_instution_pair[0] == institution_id:
                institution_name = id_instution_pair[1]

        accademic_email_suffix = Institution.objects.get(name=institution_name).accademic_email_suffix

        if not email.endswith(accademic_email_suffix):
            raise forms.ValidationError(f'{institution_name} email must end with {accademic_email_suffix}')

        return email

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.clean_email()
        
        if commit:
            user.save()

        return user

