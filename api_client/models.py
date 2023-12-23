from dajngo.db import models
from django.core.validators import MinValueValidator, ValidationError

class Booking(models.Model):
    booking_id = models.IntegerField()
    name = models.CharField(max_length=250)
    number = models.IntegerField(validators=[MinValueValidator(1)])
    details = models.TextField()

    def __str__(self):
        return self.name
    
    def clean(self):
        if self.number < 1:
            raise ValidationError('Room number must be greater than or equal to 1')