# Generated by Django 5.1.1 on 2024-12-21 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_employee_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='Last_name',
        ),
    ]
