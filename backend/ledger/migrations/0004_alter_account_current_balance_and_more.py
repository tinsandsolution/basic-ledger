# Generated by Django 4.1.7 on 2023-03-05 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0003_alter_transaction_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='current_balance',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
