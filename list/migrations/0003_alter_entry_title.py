# Generated by Django 4.2.7 on 2023-11-18 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_alter_entry_avgepisodelength'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]