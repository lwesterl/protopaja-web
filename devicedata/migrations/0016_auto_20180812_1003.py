# Generated by Django 2.0.7 on 2018-08-12 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devicedata', '0015_auto_20180812_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarm',
            name='time_ack',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='alarm',
            name='time_over',
            field=models.DateTimeField(null=True),
        ),
    ]