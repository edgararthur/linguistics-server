# Generated by Django 4.2.4 on 2024-12-21 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_publications'),
    ]

    operations = [
        migrations.AddField(
            model_name='publications',
            name='file',
            field=models.FileField(default=1, upload_to='publications_file/'),
            preserve_default=False,
        ),
    ]
