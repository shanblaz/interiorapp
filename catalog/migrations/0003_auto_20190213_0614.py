# Generated by Django 2.1.7 on 2019-02-13 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='id',
        ),
        migrations.AddField(
            model_name='part',
            name='part_id',
            field=models.PositiveIntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
