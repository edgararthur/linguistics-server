# Generated by Django 4.2.4 on 2023-01-01 06:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_collaborations'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadership',
            name='year',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]