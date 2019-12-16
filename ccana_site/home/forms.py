from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

class ReferralForm(forms.Form):
    c = [("Licensed Center", "Licensed Center"), ("Licensed Family Home", "Licensed Family Home"), ("No Preference", "No Preference")]
    referral_name = forms.CharField(required=True)
    referral_email = forms.EmailField(required=True)
    from_time = forms.TimeField(required=True)
    to_time = forms.TimeField(required=True)
    type = forms.ChoiceField(choices=c)
