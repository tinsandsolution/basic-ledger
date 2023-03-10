# Generated by Django 4.1.7 on 2023-03-04 00:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('account_number', models.CharField(max_length=16, unique=True)),
                ('current_balance', models.FloatField(default=0.0)),
                ('account_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('transaction_type', models.CharField(max_length=50)),
                ('note', models.CharField(max_length=500)),
                ('amount', models.FloatField()),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ledger.account')),
            ],
        ),
    ]
