# Generated by Django 4.1 on 2022-09-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0013_savevideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savevideo',
            name='field',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='savevideo',
            name='link',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
