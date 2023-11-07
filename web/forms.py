from django import forms
from django.forms import ModelForm
from django.forms.widgets import EmailInput
from django.forms.widgets import NumberInput
from django.forms.widgets import Textarea
from django.forms.widgets import TextInput
from .models import Contact,Career


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

        widgets = {
            "service": forms.Select(
                attrs={"class": "form-group", "placeholder": "services"}
            ),
            "name": TextInput(
                attrs={"class": "form-group", "placeholder": "Enter your name"}
            ),
            "number": NumberInput(
                attrs={"class": "form-group", "placeholder": "Enter your Number"}
            ),
            "email": EmailInput(
                attrs={"class": "form-group", "placeholder": "Enter your Email"}
            ),
            "message": Textarea(
                attrs={"class": "form-group", "placeholder": "Message"}
            ),
        }


class CareerForm(ModelForm):
    class Meta:
        model = Career
        fields = ['fullname', 'email', 'number', 'coverletter', 'cv']
        cv = forms.FileField(required=True)
        # widgets = {
        #     "fullname": TextInput(
        #         attrs={"class": "form-group", "placeholder": "Enter your name"}
        #     ),
        #     "number": NumberInput(
        #         attrs={"class": "form-group", "placeholder": "Enter your Number"}
        #     ),
        #     "email": EmailInput(
        #         attrs={"class": "form-group", "placeholder": "Enter your Email"}
        #     ),
        #     "coverletter": Textarea(
        #         attrs={"class": "form-group", "placeholder": "Cover Letter"}
        #     ),
        #     "cv": TextInput(
        #         attrs={"class": "form-group","type":"file"}
        #     ),
        # }
