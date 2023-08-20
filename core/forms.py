from django import forms
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'mode_of_payment', 'attendance', 'date_of_payment']
    
    date_of_payment = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
