# Generated by Django 5.0 on 2024-07-04 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PayRollApp', '0003_addPhoneNumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Country ID')),
                ('CountryName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Department ID')),
                ('DeprtName', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
    ]
