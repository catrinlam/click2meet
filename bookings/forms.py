from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].initial = 0  # Set default value to 0
        self.fields['quantity'].widget.attrs.update({'class': 'form-control, text-center'})
