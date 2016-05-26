from django import forms
from accounts.models import User

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

    username = forms.CharField(widget=forms.TextInput(
                                attrs={
                                'type': 'text',
                                'class': 'form-control',
                                'placeholder' : 'Username',
                                'autocomplete' : 'off',
                                }),
                                max_length=35,
                                label="Username",
                            )

    first_name = forms.CharField(widget=forms.TextInput(
                                attrs={
                                'type': 'text',
                                'class': 'form-control',
                                'placeholder' : 'Forename',
                                'autocomplete' : 'off',
                                }),
                                max_length=35,
                                label="Forename",
                            )

    last_name = forms.CharField(widget=forms.TextInput(
                                attrs={
                                'type': 'text',
                                'class': 'form-control',
                                'placeholder' : 'Surname',
                                'autocomplete' : 'off',
                                }),
                                max_length=35,
                                label="Surname",
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
                    'username',
                    'first_name',
                    'last_name',
                    'password1',
                    'password2',
                ]

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('The Username, %s is already in use.' % username)
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('The Email, %s is already in use.' % email)
        return email

    def clean(self):
        """
        Checks if password1 and password2 are the same.
        """
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data['password1'])
    #     if commit:
    #         user.save()
    #     return user


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
