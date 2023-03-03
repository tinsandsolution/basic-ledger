# Generated by Django 4.1.7 on 2023-03-03 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.IntegerField(auto_created=True, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='current_balance',
            field=models.FloatField(default=0.0),
        ),
    ]
