# Generated by Django 3.1.5 on 2021-10-03 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0021_auto_20211003_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='watermeterreplacement',
            name='network',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='watermeterreplacement',
            name='phone_number',
            field=models.CharField(max_length=250, null=True),
        ),
    ]