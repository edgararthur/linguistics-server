# Generated by Django 4.2.4 on 2023-08-30 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('position', models.CharField(max_length=200)),
                ('datejoined', models.DateField(auto_now=True)),
                ('paid_dues', models.BooleanField()),
                ('balance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.dues')),
            ],
        ),
    ]
