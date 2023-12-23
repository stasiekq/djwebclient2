#from django.forms import ModelForm
from django import forms

# class BookingForm(ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['booking_id', 'name', 'number', 'details']

class CreateBookingForm(forms.Form):
    name = forms.CharField(max_length=250)
    room = forms.IntegerField(min_value=1)
    details = forms.CharField(widget=forms.Textarea)