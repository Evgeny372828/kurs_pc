# Generated by Django 5.0.3 on 2024-05-03 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_tov_koment_kom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='koment',
            old_name='kom',
            new_name='tov',
        ),
    ]
