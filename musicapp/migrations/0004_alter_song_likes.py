# Generated by Django 4.1.1 on 2022-10-17 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_song_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
