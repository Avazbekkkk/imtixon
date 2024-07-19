# Generated by Django 5.0.7 on 2024-07-19 08:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Users'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='food',
            name='info',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='food',
            name='manufacture',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
