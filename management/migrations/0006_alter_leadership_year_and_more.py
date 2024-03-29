# Generated by Django 4.2.4 on 2024-02-06 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_leadership_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadership',
            name='year',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='members',
            name='type_of_membership',
            field=models.CharField(choices=[('regular member', 'regular member'), ('honary member', 'honary member')], max_length=20),
        ),
    ]
