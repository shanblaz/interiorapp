# Generated by Django 2.1.7 on 2019-02-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20190213_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='bedroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='pictures/bedroom')),
            ],
            options={
                'db_table': 'bedroom',
            },
        ),
        migrations.DeleteModel(
            name='part',
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='picture',
            field=models.ImageField(upload_to='pictures/kitchen'),
        ),
    ]
