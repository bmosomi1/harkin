# Generated by Django 3.1.5 on 2021-09-08 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0006_remove_waterclientall_last_meter_reading'),
    ]

    operations = [
        migrations.AddField(
            model_name='waterclientall',
            name='last_meter_reading',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
