# Generated by Django 5.1.2 on 2024-10-23 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0004_delete_salary_person_last_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
