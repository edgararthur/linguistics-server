# Generated by Django 4.2.4 on 2024-02-06 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_alter_leadership_year_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leadership',
            old_name='postion',
            new_name='position',
        ),
    ]
