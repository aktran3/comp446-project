# Generated by Django 4.2.7 on 2023-11-18 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_alter_entry_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='avgEpisodeLength',
        ),
    ]