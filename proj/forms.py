from django import forms

class ContactForm(forms.Form):
	contact_name = forms.CharField(required=True)
	contact_email = forms.CharField(required=True)
	contact_subject = forms.CharField(required=True)
	contact_message = forms.CharField(required=True)


