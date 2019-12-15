from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

class ReferralForm(forms.Form):
    referral_name = forms.CharField(required=True)
    referral_email = forms.EmailField(required=True)
    from_time = forms.TimeField(required=True)
    to_time = forms.TimeField(required=True)
    needed_days = forms.ChoiceField(choices=["Monday-Friday", "Saturday-Sunday", "Other"], required=True)
