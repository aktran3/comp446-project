# Generated by Django 4.2.7 on 2023-11-28 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0007_remove_shows_userlist_shows_userid_delete_userlist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shows',
            new_name='List',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='shows',
            new_name='list',
        ),
    ]