# Generated by Django 4.1 on 2022-09-08 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0010_trainermodel_profile1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainermodel',
            name='profile',
            field=models.ImageField(upload_to='static/health/image'),
        ),
    ]
