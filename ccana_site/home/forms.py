from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

class ReferralForm(forms.Form):
    type_c = [("Licensed Center", "Licensed Center"), ("Licensed Family Home", "Licensed Family Home"), ("No Preference", "No Preference")]
    days_c = [("Monday - Friday","Monday - Friday"), ("Saturday - Sunday", "Saturday - Sunday")]
    county_c = [
        ("Baxter", "Baxter"),
        ("Cleburne", "Cleburne"),
        ("Conway", "Conway"),
        ("Faulkner", "Faulkner"),
        ("Fulton", "Fulton"),
        ("Independence", "Independence"),
        ("Izard", "Izard"),
        ("Jackson", "Jackson"),
        ("Marion", "Marion"),
        ("Searcy", "Searcy"),
        ("Sharp", "Sharp"),
        ("Stone", "Stone"),
        ("Van Buren", "Van Buren"),
        ("White", "White")]
    referral_name = forms.CharField(required=True)
    referral_email = forms.EmailField(required=True)
    From_time = forms.TimeField(required=True)
    To_time = forms.TimeField(required=True)
    type = forms.ChoiceField(choices=type_c, required=True)
    days = forms.ChoiceField(choices=days_c, required=True)
    first_date = forms.DateField(label="First Child DOB (dd/mm/yyyy)", required=True)
    second_date = forms.DateField(label="Second Child DOB (dd/mm/yyyy)")
    third_date = forms.DateField(label="Third Child DOB (dd/mm/yyyy)")
    employer = forms.CharField(required=True)
    spouse_employer = forms.CharField(required=True)
    address = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    zip = forms.CharField(required=True)
    county = forms.ChoiceField(choices=county_c, required=True)
    phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', required=False,
        error_messages = {"invalid":"Please enter your phone number with no punctuation. It should be between 9 and 15 digits long."})
