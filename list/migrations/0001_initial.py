# Generated by Django 4.2.7 on 2023-11-18 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('rating', models.IntegerField()),
                ('episodeCount', models.IntegerField()),
                ('avgEpisodeLength', models.TimeField()),
            ],
        ),
    ]
