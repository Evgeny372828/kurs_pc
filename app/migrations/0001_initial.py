# Generated by Django 5.0.3 on 2024-04-30 14:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Imgtovar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Kategor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('img', models.ImageField(null=True, upload_to='')),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('kategor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.kategor')),
            ],
        ),
        migrations.CreateModel(
            name='Pod_kat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('kateg', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.kategor')),
                ('stat', models.ManyToManyField(to='app.stat')),
            ],
        ),
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.IntegerField()),
                ('comp', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.company')),
                ('img', models.ManyToManyField(to='app.imgtovar')),
                ('keteg', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.kategor')),
                ('pod_kat', models.ManyToManyField(to='app.pod_kat')),
                ('stat', models.ManyToManyField(to='app.stat')),
            ],
        ),
        migrations.CreateModel(
            name='Koment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('koment', models.TextField()),
                ('star', models.TextField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='app.koment')),
                ('tov', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tovar')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарий',
            },
        ),
    ]
