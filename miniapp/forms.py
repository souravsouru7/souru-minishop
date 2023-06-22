from django import forms
from .models import BillingDetails
from .models import BankDetails
class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingDetails
        fields = ('first_name', 'last_name', 'country', 'state', 'pin_code', 'phone_number', 'email')



class BankForm(forms.ModelForm):
    class Meta:
        model = BankDetails
        fields = ('account_number', 'account_holder_name', 'bank_name', 'branch')