# Generated by Django 2.2.4 on 2019-10-25 01:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0012_auto_20191024_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outgoing1',
            name='sent_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 10, 25, 1, 0, 46, 607869)),
        ),
    ]
