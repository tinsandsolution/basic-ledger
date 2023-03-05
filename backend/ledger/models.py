from django.db import models
from authentication.models import CustomUser
from django.core.validators import MaxValueValidator
from django.utils import timezone


# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    account_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account_number = models.CharField(unique=True, max_length=16)
    current_balance = models.FloatField(default=0.0)

class Transaction(models.Model):
    # id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    transaction_type = models.CharField(max_length=50)
    note = models.CharField(max_length=500)
    amount = models.FloatField()
