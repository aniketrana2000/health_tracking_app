# Generated by Django 4.1 on 2022-09-07 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0006_walletmodel_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='walletmodel',
            name='Balance',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='Balance',
            field=models.FloatField(null=True),
        ),
    ]
