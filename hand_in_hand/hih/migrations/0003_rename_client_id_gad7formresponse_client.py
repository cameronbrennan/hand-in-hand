# Generated by Django 3.2.3 on 2021-07-16 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hih', '0002_rename_client_gad7formresponse_client_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gad7formresponse',
            old_name='client_id',
            new_name='client',
        ),
    ]
