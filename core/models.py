from django.db import models


class Attendance(models.Model):
    PAYMENT_CHOICES = (('momo', 'Mobile Money'), ('bank', 'Bank Transfer'))
    ATTENDANCE = (('observer', 'Observer'), ('speaker', 'Presenter'))

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    mode_of_payment = models.CharField(max_length=4, choices=PAYMENT_CHOICES)
    attendance = models.CharField(max_length=10, choices=ATTENDANCE)
    date_of_payment = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.phone_number} {self.mode_of_payment} {self.attendance} {self.date_of_payment}"

