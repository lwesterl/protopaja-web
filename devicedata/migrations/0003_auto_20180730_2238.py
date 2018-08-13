# Generated by Django 2.0.7 on 2018-07-30 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devicedata', '0002_auto_20180716_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='device_number',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='temperature',
            field=models.IntegerField(),
        ),
    ]
