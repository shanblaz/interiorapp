# Generated by Django 2.1.7 on 2019-02-13 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20190213_0630'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='kitchen',
        ),
        migrations.AlterModelTable(
            name='kitchen',
            table='kitchen',
        ),
    ]
