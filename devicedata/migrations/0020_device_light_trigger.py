# Generated by Django 2.0.7 on 2018-08-13 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devicedata', '0019_auto_20180813_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='light_trigger',
            field=models.IntegerField(default=2),
        ),
    ]
