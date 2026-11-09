from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["full_name", "phone", "address", "city", "state", "pincode"]
        widgets = {
            "address": forms.Textarea(attrs={"rows": 3}),
        }

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if not phone.isdigit() or len(phone) != 10:
            raise forms.ValidationError("Enter a valid 10-digit phone number.")
        return phone

    def clean_pincode(self):
        pincode = self.cleaned_data["pincode"]
        if not pincode.isdigit() or len(pincode) != 6:
            raise forms.ValidationError("Enter a valid 6-digit pincode.")
        return pincode