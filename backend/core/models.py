from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, unique=True)
    hashed_password = models.CharField(max_length=500)

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    account_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=16, unique=True)
    current_balance = models.FloatField()

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateTimeField()
    transaction_type = models.CharField(max_length=50)
    note = models.CharField(max_length=500)
    amount = models.FloatField()
