# Generated by Django 4.2.6 on 2023-10-20 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='seating_capacity',
            new_name='capacity',
        ),
    ]