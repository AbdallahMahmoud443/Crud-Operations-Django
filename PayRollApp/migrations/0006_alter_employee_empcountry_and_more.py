# Generated by Django 5.0 on 2024-07-04 18:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PayRollApp', '0005_remove_employee_country_employee_empcountry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='EmpCountry',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='Employee_Country', to='PayRollApp.countries'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='EmpDepartment',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='Employee_Department', to='PayRollApp.departments'),
        ),
    ]
