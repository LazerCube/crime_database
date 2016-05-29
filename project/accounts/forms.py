from django import forms
from accounts.models import User
from management.models import Students

from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new user.
    """

    email = forms.CharField(widget=forms.TextInput(
                                attrs={
                                'type': 'email',
                                'class': 'form-control',
                                'placeholder' : 'Email',
                                'autocomplete' : 'off',
                                }),
                                max_length=255,
                                label="Email",
                            )

    account_code = forms.CharField(widget=forms.TextInput(
                                    attrs={
                                    'type': 'text',
                                    'class': 'form-control',
                                    'placeholder' : 'Code',
                                    'autocomplete' : 'off',
                                    }),
                                    max_length=6,
                                    label="Code",
                                )

    password1 = forms.CharField(widget=forms.PasswordInput(
                            attrs={
                                'type': 'password',
                                'class': 'form-control',
                                'placeholder' : 'Password',
                                'autocomplete' : 'off',
                                }),
                                label="Password",
                            )

    password2 = forms.CharField(widget=forms.PasswordInput(
                            attrs={
                                'type': 'password',
                                'class': 'form-control',
                                'placeholder' : 'Password (again)',
                                'autocomplete' : 'off',
                                }),
                                label="Password (again)",
                            )
    class Meta:
        model = User
        fields = [  'email',
                    'password1',
                    'password2',
                    'account_code',
                ]

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('The Email, %s is already in use.' % email)
        return email

    def clean_account_code(self):
        account_code = self.cleaned_data['account_code']
        student = Students.objects.get(student_id=account_code)
        if not Students.objects.filter(student_id=account_code).exists():
            raise forms.ValidationError("Student code doesn't exists.")
        if not student.account is None:
            raise forms.ValidationError("Student already has an account")
        return account_code

    def clean(self):
        """
        Checks if password1 and password2 are the same.
        """
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
            validate_password(self.cleaned_data.get('password2'), self.instance)
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        student = Students.objects.get(student_id=self.cleaned_data["account_code"])
        if commit:
            user.save()
            student.add_account(user)
        return user


class AuthenticationForm(forms.Form):
    """
    Form for logging in a user.
    """
    username = forms.CharField(widget=forms.TextInput(
                                attrs={
                                'type': 'text',
                                'class': 'form-control',
                                'placeholder' : 'Email',
                                'autocomplete' : 'off',
                                }),
                                max_length=35,
                                label="Email",
                            )

    password = forms.CharField(widget=forms.PasswordInput(
                            attrs={
                                'type': 'password',
                                'class': 'form-control',
                                'placeholder' : 'Password',
                                'autocomplete' : 'off',
                                }),
                                label="Password",
                            )

    class Meta:
        fields = ['username', 'password']

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class EditForm(forms.ModelForm):
    """
    Form for editting a user.
    """

    new_email = forms.CharField(widget=forms.TextInput(
                                    attrs={
                                    'type': 'email',
                                    'class': 'form-control',
                                    'placeholder' : 'New Email',
                                    'autocomplete' : 'off',
                                    }),
                                    max_length=255,
                                    label="New Email",
                                    required=False,
                                )

    password1 = forms.CharField(widget=forms.PasswordInput(
                            attrs={
                                'type': 'password',
                                'class': 'form-control',
                                'placeholder' : 'New Password',
                                'autocomplete' : 'off',
                                }),
                                label="New Password",
                                required=False,
                            )

    password2 = forms.CharField(widget=forms.PasswordInput(
                            attrs={
                                'type': 'password',
                                'class': 'form-control',
                                'placeholder' : 'New Password (again)',
                                'autocomplete' : 'off',
                                }),
                                label="New Password (again)",
                                required=False,
                            )

    class Meta:
        model = User
        fields = [  'new_email',
                    'password1',
                    'password2',
                ]

    def clean_new_email(self):
        email = self.cleaned_data['new_email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('The Email, %s is already in use.' % email)
        return email

    def clean(self):
        """
        Checks if password1 and password2 are the same.
        """
        cleaned_data = super(EditForm, self).clean()

        if 'password1' in cleaned_data and 'password2' in cleaned_data:
            if cleaned_data['password1'] or cleaned_data['password2']:
                if cleaned_data['password1'] != cleaned_data['password2']:
                    raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
                validate_password(cleaned_data['password2'], self.instance)
        return cleaned_data

    def save(self, commit=True):
        user = super(EditForm, self).save(commit=False)
        password = self.cleaned_data["password2"]
        new_email = self.cleaned_data["new_email"]
        if password:
            user.set_password(password)
        if new_email:
            user.email = new_email
        if commit:
            user.save()
        return user
