# Generated by Django 4.2.7 on 2023-11-22 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipl_app', '0004_rename_match_id_deliveries_match'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliveries',
            old_name='match',
            new_name='match_id',
        ),
        migrations.RenameField(
            model_name='matches',
            old_name='player_of_the_match',
            new_name='player_of_match',
        ),
    ]
