# Generated by Django 2.0.7 on 2018-08-02 15:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('devicedata', '0002_device_user_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='device_number',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this device', primary_key=True, serialize=False),
        ),
    ]
