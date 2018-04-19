# make sure this is at the top if it isn't already
# from django import forms

# # our new form
# class ContactForm(forms.Form):
#     contact_name = forms.CharField(required=True)
#     contact_email = forms.EmailField(required=True)
#     content = forms.CharField(
#         required=True,
#         widget=forms.Textarea
#     )


# -*- coding: utf-8 -*-

from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=64, required=False, label='Imię i nazwisko')
    company = forms.CharField(max_length=128, label='Tytuł wiadomości')
    contact = forms.CharField(max_length=128, label='Adres email')
    message = forms.CharField(widget=forms.Textarea, label='Wiadomość')
