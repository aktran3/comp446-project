# Generated by Django 4.2.7 on 2023-11-28 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_userlist_shows_entry_shows'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shows',
            old_name='listName',
            new_name='listname',
        ),
        migrations.AddField(
            model_name='shows',
            name='listid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]