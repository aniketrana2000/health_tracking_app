# Generated by Django 4.1 on 2022-09-12 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0015_trainermodel_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='link',
            field=models.URLField(max_length=800),
        ),
    ]