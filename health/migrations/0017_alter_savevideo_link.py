# Generated by Django 4.1 on 2022-09-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0016_alter_videos_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savevideo',
            name='link',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
