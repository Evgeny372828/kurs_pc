# Generated by Django 5.0.3 on 2024-05-06 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_kom_koment_tov'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tovar',
            name='img',
        ),
        migrations.AddField(
            model_name='tovar',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
