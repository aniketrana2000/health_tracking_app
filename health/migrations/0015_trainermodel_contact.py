# Generated by Django 4.1 on 2022-09-12 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0014_alter_savevideo_field_alter_savevideo_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainermodel',
            name='contact',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
