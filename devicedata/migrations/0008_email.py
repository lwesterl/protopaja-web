# Generated by Django 2.0.7 on 2018-08-10 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devicedata', '0007_auto_20180803_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.EmailField(max_length=254)),
                ('devices', models.ManyToManyField(to='devicedata.Device')),
            ],
        ),
    ]