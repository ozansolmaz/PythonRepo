from django.db import models
from django.utils import timezone

# Create your models here.

class LogMessage(models.Model):
    message = models.CharField("Mesaj Alanı", max_length=50)
    log_date = models.DateTimeField("Log'un tarihi", auto_now=False, auto_now_add=False)
    #field types: textfield (unlimited text), emailfield, urlfield, integerfield, decimalfield, booleanfield, datetimefield, foreignkey, manytomany
    def __str__(self) -> str:
        #returns the string representation of the LogMessage
        date=timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
