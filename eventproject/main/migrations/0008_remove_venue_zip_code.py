# Generated by Django 4.1.7 on 2023-02-21 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_myeventuser_eventuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='zip_code',
        ),
    ]