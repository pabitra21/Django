# Generated by Django 5.1.2 on 2024-10-22 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0003_remove_person_last_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Salary',
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]