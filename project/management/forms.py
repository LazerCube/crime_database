from django import forms
from django.forms import extras

from management.models import Students

class AddStudentForm(forms.ModelForm):
    """
    Form adding a new student.
    """

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

    # date_of_birth = forms.DateInput(
    #                                 label="Date of birth",
    #                             )

    # date_of_birth = forms.CharField(widget=forms.TextInput(
    #                             attrs={
    #                             'type': 'text',
    #                             'class': 'form-control',
    #                             'placeholder' : 'Date of birth',
    #                             'autocomplete' : 'off',
    #                             'data-format':"dd-MM-yyyy"
    #                             }),
    #                             label="Date of birth",
    #                         )

    date_of_birth = forms.CharField(widget=forms.TextInput(
                                attrs={
                                'type': 'text',
                                'class': 'datepicker form-control',
                                'placeholder' : 'Date of birth',
                                'autocomplete' : 'off',
                                }),
                                label="Date of birth",
                            )

    class Meta:
        model = Students
        fields = [  'first_name',
                    'last_name',
                    'date_of_birth',
                ]

    def save(self, commit=True):
        user = super(AddStudentForm, self).save(commit=False)
        if commit:
            user.save()
        return user
