# Generated by Django 5.0.3 on 2024-05-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_koment_content_koment_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='koment',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='koment',
            name='rating',
            field=models.TextField(),
        ),
    ]
