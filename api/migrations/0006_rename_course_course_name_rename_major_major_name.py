# Generated by Django 4.1.3 on 2022-12-04 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_delete_majorcourse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='major',
            old_name='major',
            new_name='name',
        ),
    ]
